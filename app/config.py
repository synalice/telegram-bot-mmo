from dotenv import dotenv_values


config = dotenv_values(".env")

# Create .env file in the same directory and add BOT_API_TOKEN variable there to use bot
BOT_API_TOKEN = config.get("BOT_API_TOKEN")
