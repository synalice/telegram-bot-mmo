import asyncio

import sqlalchemy.ext.asyncio as sa_async
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config import DB_CONN_STR
from app.db.db_schemas import Base


engine = sa_async.create_async_engine(f"{DB_CONN_STR}", echo=True)


async def init_db():
    """
    This function runs synchronous metadata.create_all to create all the tables describes in db_schemas
    Thanks to @burenotti for helping with writing this.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


loop = asyncio.get_event_loop()
loop.run_until_complete(init_db())

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
