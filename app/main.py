from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ParseMode

import keyboard as kb
import hero as hero
from config import BOT_API_TOKEN


bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
	await message.answer(
		"Приветствую! Выбери замок, за который будешь сражаться.",
		reply_markup=kb.choose_castle_on_start()
	)


# Ответ на любые неизвестные коммады или сообщения от пользователя
# Не двигать выше, иначе оно сломается.
@dp.message_handler()
async def unknown_command_answer(message: types.Message):
	await message.answer("I don't recognise this command.")


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
