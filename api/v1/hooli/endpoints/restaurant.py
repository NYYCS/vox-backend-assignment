from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from models.restaurant import Restaurant, RestaurantUpdate
from db import get_db_session

router = APIRouter()

async def get_restaurant(restaurant_id, session = Depends(get_db_session)):
    stmt = select(Restaurant).where(Restaurant.id == restaurant_id)
    restaurant = await session.execute(stmt)
    return restaurant.scalars().first()

@router.put('/{restaurant_id}', status_code=202)
async def update_restaurant(payload: RestaurantUpdate, restaurant = Depends(get_restaurant), session = Depends(get_db_session)):
    if restaurant is None:
        raise HTTPException(404)
    restaurant.name = payload.name
    restaurant.hooli_number = payload.hooli_number
    await session.commit()