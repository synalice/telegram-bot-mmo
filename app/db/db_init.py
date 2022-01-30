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


engine = sa_async.create_async_engine(
    f"{DB_NAME}{DB_DRIVER}://{DB_LOGIN}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}",
    echo=True,
)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
