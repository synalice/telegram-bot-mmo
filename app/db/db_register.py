import asyncio

from sqlalchemy.exc import IntegrityError
from app.db.db_init import *
from app.db.db_schemas import TelegramUserProfile
from concurrent.futures import ThreadPoolExecutor
from app.utils import make_async

db_thead_pool = ThreadPoolExecutor(max_workers=32)


@make_async(executor=db_thead_pool)
def register_new_user(user_id, first_name, last_name):
    session = Session()
    user = (
        session.query(TelegramUserProfile)
        .filter(TelegramUserProfile.telegram_id == user_id)
        .one_or_none()
    )

    if not user:
        user = TelegramUserProfile(
            telegram_id=user_id,
            telegram_firstname=first_name,
            telegram_lastname=last_name,
        )
        session.add(user)
        session.commit()

    session.close()
    return user
