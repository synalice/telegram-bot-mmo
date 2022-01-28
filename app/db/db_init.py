import asyncio

import sqlalchemy.ext.asyncio as sa_async
import sqlalchemy as sa
from app.config import (
    DB_NAME,
    DB_DRIVER,
    DB_LOGIN,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_DATABASE,
)


async def async_main():
    engine = sa_async.create_async_engine(
        f"{DB_NAME}{DB_DRIVER}://{DB_LOGIN}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}",
        echo=False,
    )
    metadata_obj = sa.MetaData()


asyncio.run(async_main())
# Session = sessionmaker(bind=engine)
# Base = declarative_base()
