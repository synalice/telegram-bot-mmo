import os

from dotenv import dotenv_values

# .env should be in root directory - /telegram_bot_mmo/.env
config = {**dotenv_values("../.env"), **os.environ}

BOT_API_TOKEN = config.get("BOT_API_TOKEN")
DB_NAME_N_DRIVER = config.get("DB_NAME_N_DRIVER")
DB_LOGIN = config.get("DB_LOGIN")
DB_PASSWORD = config.get("DB_PASSWORD")
DB_HOST = config.get("DB_HOST")
DB_PORT = config.get("DB_PORT")
DB_DATABASE = config.get("DB_DATABASE")

"""
Example of how it should look like in .env file:

BOT_API_TOKEN="12345asdfgfhesfdgh"
DB_NAME_N_DRIVER="postgresql+asyncpg"
DB_LOGIN="user"
DB_PASSWORD="password"
DB_HOST="localhost"
DB_PORT="5432"
DB_DATABASE="database_name"
"""
