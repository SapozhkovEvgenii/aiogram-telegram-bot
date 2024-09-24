import os

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from dotenv import load_dotenv, find_dotenv

from db_models.user import Base

load_dotenv(find_dotenv())

# DB_URL=postgresql+asyncpg://login:password@localhost:5432/db_name

# engine = create_async_engine(os.getenv('DB_LITE'), echo=True)

engine = create_async_engine(os.getenv('DB_URL'), echo=True)  # type: ignore

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
