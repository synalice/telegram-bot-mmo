import asyncio

import sqlalchemy as sa
import sqlalchemy.ext.asyncio as sa_async
from aiogram import Bot, Dispatcher, types, executor
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import BOT_API_TOKEN
from app.config import (
    DB_NAME,
    DB_DRIVER,
    DB_LOGIN,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_DATABASE,
)


Base = declarative_base()


async def async_main():
    bot = Bot(token=BOT_API_TOKEN)
    dp = Dispatcher(bot)

    executor.start_polling(dp, skip_updates=True)

    @dp.message_handler(commands=["start"])
    async def start_command(message: types.Message):
        user = await register_new_user(
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.last_name,
        )
        await message.answer(
            f"{user.telegram_id, user.telegram_firstname, user.telegram_lastname}"
        )

    # Ответ на любые неизвестные коммады или сообщения от пользователя
    # Не двигать выше, иначе оно сломается.
    @dp.message_handler()
    async def unknown_command_answer(message: types.Message):
        await message.answer("I don't recognise this command.")

    engine = sa_async.create_async_engine(
        f"{DB_NAME}{DB_DRIVER}://{DB_LOGIN}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}",
        echo=False,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    class TelegramUserProfile(Base):
        __tablename__ = "telegram_user_profile"
        telegram_id = sa.Column(sa.Integer, primary_key=True)
        telegram_firstname = sa.Column(sa.String, nullable=False)
        telegram_lastname = sa.Column(sa.String)
        sa.Index(telegram_id, unique=True)

    async def register_new_user(user_id, first_name, last_name):
        async_session = sessionmaker(engine, expire_on_commit=True, class_=AsyncSession)

        async with async_session() as session:
            async with session.begin():
                querry_user = (
                    sa.select(TelegramUserProfile)
                    .where(TelegramUserProfile.telegram_id == user_id)
                    .one()
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


if __name__ == "__main__":
    asyncio.run(async_main())
