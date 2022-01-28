import sqlalchemy as sa
from app.db.db_init import create_async_session


from app.db.db_schemas import TelegramUserProfile


async def register_new_user(user_id, first_name, last_name):
    async with (await create_async_session()) as session:
        async with session.begin():
            querry_user = sa.select(TelegramUserProfile).where(
                TelegramUserProfile.telegram_id == user_id
            )
            user = await session.execute(querry_user)
            await session.commit()
    if not user:
        user = TelegramUserProfile(
            telegram_id=user_id,
            telegram_firstname=first_name,
            telegram_lastname=last_name,
        )
    return user
