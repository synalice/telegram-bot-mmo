# Импорт модулей для клавиатуры
from aiogram.types import KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Замки
castle_bees = KeyboardButton('🐝')
castle_hedgehogs = KeyboardButton('🦔')
castle_unicorns = KeyboardButton('🦄')
castle_bugs = KeyboardButton('🐛')

# Основной экран
button_attack = KeyboardButton('[⚔] Атака')
button_defend = KeyboardButton('[🛡] Защита')
button_quests = KeyboardButton('[🗺] Квесты')
button_hero = KeyboardButton('[🏅] Герой')
button_castle = KeyboardButton('[🏰] Замок')
button_guild = KeyboardButton('[🏛] Гильдия')


def choose_castle_on_start():
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(castle_bees, castle_hedgehogs)
	keyboard.add(castle_unicorns, castle_bugs)
	return keyboard


if __name__ == '__main__':
	pass
