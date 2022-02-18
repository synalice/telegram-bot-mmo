import os

"""
.env should be in root directory - /telegram_bot_mmo/.env
variables should look like this: VAR=value

To connect to the database you should pass in a connection url as an env variable: DB_CONN_STR
The structure has to be like this: DB_CONN_STR=driver://user:pass@host/dbname

Recommended url to use would be this: postgresql+asyncpg://<user>:<pass>@db/<dbname>
You only have to specify your user, password and database name.
"""
config = {**os.environ}

BOT_API_TOKEN = config.get("BOT_API_TOKEN")
DB_CONN_STR = config.get("DB_CONN_STR")
