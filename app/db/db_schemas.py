from app.db.db_init import *


class TelegramUserProfile(Base):
	__tablename__ = 'telegram_user_profile'

	telegram_id = sa.Column(sa.Integer, primary_key=True)
	telegram_firstname = sa.Column(sa.String, nullable=False)
	telegram_lastname = sa.Column(sa.String)

# class UserProfile(Base):
# 	pass

# TODO: add other tables later

# Base.metadata.create_all(engine)
