from fastapi import APIRouter
from api.v1 import hooli

router = APIRouter()

router.include_router(hooli.router, prefix="/hooli")