import asyncio

from sqlalchemy.exc import IntegrityError
from app.db.db_init import *
from app.db.db_schemas import TelegramUserProfile
from concurrent.futures import ThreadPoolExecutor

db_thead_pool = ThreadPoolExecutor(max_workers=32)


def create_user_sync(user_id, first_name, last_name):
	session = Session()
	user = (
		session
		.query(TelegramUserProfile)
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


async def register_new_user(user_id, first_name, last_name):
	loop = asyncio.get_running_loop()
	user = await loop.run_in_executor(db_thead_pool, create_user_sync, user_id, first_name, last_name)
	return user
