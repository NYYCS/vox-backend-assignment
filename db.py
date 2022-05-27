from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite+aiosqlite:///database.sqlite"

engine = create_async_engine(DB_URL, echo=True)
_AsyncSession = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_db_session():
    async with _AsyncSession() as session:
        yield session