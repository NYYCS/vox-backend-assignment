from fastapi import FastAPI
from api import router

from db import init_db

app = FastAPI()

app.include_router(router, prefix="/api")

@app.on_event('startup')
async def on_startup():
    await init_db()

