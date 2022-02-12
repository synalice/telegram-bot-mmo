import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TelegramProfile(Base):
    __tablename__ = "telegram_profile"

    id = sa.Column(sa.Integer, primary_key=True)
    telegram_firstname = sa.Column(sa.String, nullable=False)
    telegram_lastname = sa.Column(sa.String)
    sa.Index(id, unique=True)

    player_profile = relationship(
        "PlayerProfile",
        back_populates="telegram_profile",
        uselist=False,
    )


class PlayerProfile(Base):
    __tablename__ = "player_profile"

    telegram_id = sa.Column(sa.Integer, sa.ForeignKey("telegram_profile.id"))

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    player_firstname = sa.Column(sa.String, nullable=False)
    player_lvl = sa.Column(sa.Integer)
    sa.Index(id, unique=True)

    telegram_profile = relationship("TelegramProfile", back_populates="player_profile")
