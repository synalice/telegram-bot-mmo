import sqlalchemy.ext.asyncio as sa_async
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config import (
    DB_NAME,
    DB_DRIVER,
    DB_LOGIN,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_DATABASE,
)
from app.db.db_schemas import Base


engine = None


async def async_main():
    global engine
    engine = sa_async.create_async_engine(
        f"{DB_NAME}{DB_DRIVER}://{DB_LOGIN}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}",
        echo=False,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_async_session():
    async_session = sessionmaker(engine, expire_on_commit=True, class_=AsyncSession)
    return async_session
