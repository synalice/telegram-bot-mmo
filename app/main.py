from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from app.config import BOT_API_TOKEN
from app.services.users import register_new_user


bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    user_exists, user =      await register_new_user(
        message.from_user.id,
        message.from_user.first_name,
        message.from_user.last_name,
    )
    if not user_exists
        answer_message = f"{user.id, user.telegram_firstname, user.telegram_lastname}"
        await message.answer(answer_message)
    elif user_exists:
        answer_message = f"Hello, {user.telegram_firstname}"
    else:
        answer_message = "Something went wrong..."
        await message.answer(answer_message)
    await message.answer(answer_message)


# Ответ на любые неизвестные коммады или сообщения от пользователя
# Не двигать выше, иначе оно сломается.
@dp.message_handler()
async def unknown_command_answer(message: types.Message):
    await message.answer("I don't recognise this command.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
