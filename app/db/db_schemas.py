import sqlalchemy as sa


class TelegramUserProfile(Base):
    __tablename__ = "telegram_user_profile"
    telegram_id = sa.Column(sa.Integer, primary_key=True)
    telegram_firstname = sa.Column(sa.String, nullable=False)
    telegram_lastname = sa.Column(sa.String)
    sa.Index(
        telegram_id, unique=True
    )  # Not sure if unique=True is needed since telegram_id is pk.


# class UserProfile(Base):
# 	pass

# TODO: add other tables later

# Base.metadata.create_all(engine)
