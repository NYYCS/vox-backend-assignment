from fastapi import APIRouter
from api.v1.hooli.endpoints import message, restaurant

router = APIRouter()

router.include_router(message.router, prefix="/message")
router.include_router(restaurant.router, prefix="/restaurant")