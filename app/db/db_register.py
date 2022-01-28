import sqlalchemy as sa
from sqlalchemy.orm import Session

from app.db.db_schemas import TelegramUserProfile


class ThingOne(object):
    def go(self, session):
        session.query(FooBar).update({"x": 5})


class ThingTwo(object):
    def go(self, session):
        session.query(Widget).update({"q": 18})


def run_my_program():
    with Session() as session:
        with session.begin():
            ThingOne().go(session)
            ThingTwo().go(session)


def register_new_user(user_id, first_name, last_name):
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
    return user


def run_my_program():
    with Session() as session:
        with session.begin():
            ThingOne().go(session)
            ThingTwo().go(session)
