from sqlalchemy.exc import IntegrityError

from app.db.db_init import *
from app.db.db_schemas import TelegramUserProfile


def register_new_user(user_id, first_name, last_name):
	"""This function checks if user exists in the database and adds him there if he doesn't"""
	try:
		new_user = TelegramUserProfile(
			telegram_id=user_id,
			telegram_firstname=first_name,
			telegram_lastname=last_name
		)
		session.add(new_user)
		session.commit()
		return "Registered!"
	except IntegrityError:
		session.rollback()
		return f"С возвращением, {first_name}!"
