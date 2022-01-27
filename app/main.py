from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ParseMode

import app.keyboard as kb

# import app.hero as hero
from app.config import BOT_API_TOKEN
from app.db.db_register import register_new_user


bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    user = await register_new_user(
        message.from_user.id, message.from_user.first_name, message.from_user.last_name
    )
    await message.answer(
        f"{user.telegram_id, user.telegram_firstname, user.telegram_lastname}"
    )


# Ответ на любые неизвестные коммады или сообщения от пользователя
# Не двигать выше, иначе оно сломается.
@dp.message_handler()
async def unknown_command_answer(message: types.Message):
    await message.answer("I don't recognise this command.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
