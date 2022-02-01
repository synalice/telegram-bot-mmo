import sqlalchemy as sa

from app.db.db_init import async_session
from app.db.db_schemas import TelegramUserProfile


async def register_new_user(user_id, first_name, last_name):
    async with async_session() as session:
        querry_user = sa.select(TelegramUserProfile).where(
            TelegramUserProfile.telegram_id == user_id
        )
        user = (await session.execute(querry_user)).scalars().first()
        if not user:
            user = TelegramUserProfile(
                telegram_id=user_id,
                telegram_firstname=first_name,
                telegram_lastname=last_name,
            )
            session.add(user)
            await session.commit()
    return user
