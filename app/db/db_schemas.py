import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TelegramUserProfile(Base):
    __tablename__ = 'telegram_profile'
    telegram_id = sa.Column(sa.Integer, primary_key=True)
    telegram_firstname = sa.Column(sa.String, nullable=False)
    telegram_lastname = sa.Column(sa.String)
    sa.Index(telegram_id, unique=True)
#     children = relationship("Child", back_populates="parent")
#
# class PlayerUserProfile(Base):
#     __tablename__ = 'player_user_profile'
#     player_id = sa.Column(sa.Integer, primary_key=True)
#     player_firstname = sa.Column(sa.String, nullable=False)
#     player_lvl = sa.Integer
#     sa.Index(telegram_id, unique=True)
