import os


# .env should be in root directory - /telegram_bot_mmo/.env
# envs should look like this: VAR=value
config = {**os.environ}

BOT_API_TOKEN = config.get("BOT_API_TOKEN")
DB_NAME_N_DRIVER = config.get("DB_NAME_N_DRIVER")
DB_LOGIN = config.get("DB_LOGIN")
DB_PASSWORD = config.get("DB_PASSWORD")
DB_HOST = config.get("DB_HOST")
DB_PORT = config.get("DB_PORT")
DB_DATABASE = config.get("DB_DATABASE")
