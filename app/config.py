from dotenv import dotenv_values


# Why doesn't it work as ("app/.env")?!
config = dotenv_values(".env")

# Create .env file in the same directory and add BOT_API_TOKEN variable there to use bot
BOT_API_TOKEN = config.get("BOT_API_TOKEN")
