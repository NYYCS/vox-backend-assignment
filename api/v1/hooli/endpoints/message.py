from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.future import select

from db import get_db_session
from ratelimit import RatelimitMapping

from models.customer import Customer
from models.restaurant import Restaurant
from models.message import MessageGet, Message

import aiohttp

PREDICT_API_URL = 'http://demo1616407.mockable.io/v1/predict'

router = APIRouter()

customer_ratelimit = RatelimitMapping(rate=1.0)


async def get_customer(payload: MessageGet, session = Depends(get_db_session)):
    stmt = select(Customer).where(Customer.hooli_number == payload.sender)
    customer = await session.execute(stmt)
    return customer.scalars().first()

async def get_restaurant(payload: MessageGet, session = Depends(get_db_session)):
    stmt = select(Restaurant).where(Restaurant.hooli_number == payload.receiver)
    restaurant = await session.execute(stmt)
    return restaurant.scalars().first()


async def get_http_session():
    try:
        http = aiohttp.ClientSession()
        yield http
    finally:
        await http.close()

@router.post('/', response_model=list[Message])
async def get_message(payload: MessageGet, customer = Depends(get_customer), restaurant = Depends(get_restaurant), http = Depends(get_http_session)):
    if customer is None or restaurant is None:
        raise HTTPException(404)

    await customer_ratelimit.get_token(customer.id)

    payload = {
        "channel": f"{restaurant.id}__{customer.id}",
        "message": payload.text,
        "customer_record": customer.dict(),
        "restaurant_record": restaurant.dict(),
    }
    
    response = await http.get(PREDICT_API_URL)
    data = await response.json()
    
    return data['responses']
    