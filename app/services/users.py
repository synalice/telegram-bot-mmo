import sqlalchemy as sa

from app.db.db_init import async_session
from app.db.db_schemas import TelegramProfile


async def register_new_user(user_id, first_name, last_name):
    async with async_session() as session:
        querry_user = sa.select(TelegramProfile).where(TelegramProfile.id == user_id)
        user = (await session.execute(querry_user)).scalars().first()
        if user:
            return True, user
        elif not user:
            user = TelegramProfile(
                id=user_id,
                telegram_firstname=first_name,
                telegram_lastname=last_name,
            )
            session.add(user)
            await session.commit()
            return False, user
    return 1
