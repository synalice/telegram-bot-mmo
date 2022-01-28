import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.db.db_init import engine
from app.db.db_schemas import TelegramUserProfile


async def register_new_user(user_id, first_name, last_name):
    async_session = sessionmaker(engine, expire_on_commit=True, class_=AsyncSession)
    async with async_session() as session:
        async with session.begin():
            querry_user = sa.select(TelegramUserProfile).where(
                TelegramUserProfile.telegram_id == user_id
            )
            user = await session.execute(querry_user)
            await session.commit()
    if not user:
        async_session = sessionmaker(engine, expire_on_commit=True, class_=AsyncSession)
        async with async_session() as session:
            async with session.begin():
                user = TelegramUserProfile(
                    telegram_id=user_id,
                    telegram_firstname=first_name,
                    telegram_lastname=last_name,
                )
                await session.add(user)
                await session.commit()
    return user
