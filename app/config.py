import os
from dotenv import dotenv_values


config = {**dotenv_values(".env"), **os.environ}

# Create .env file in the same directory and add BOT_API_TOKEN variable there to use bot
BOT_API_TOKEN = config.get("BOT_API_TOKEN")

DB_NAME = config.get("DB_NAME")
DB_LOGIN = config.get("DB_LOGIN")
DB_PASSWORD = config.get("DB_PASSWORD")
DB_HOST = config.get("DB_HOST")
DB_PORT = config.get("DB_PORT")
DB_DATABASE = config.get("DB_NAME")
