from pyrogram import Client
import json
from FUNC.server_stats import *

plugins = dict(root="BOT")

# Leer las configuraciones desde config.json
with open("config.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)
    API_ID = DATA["API_ID"]
    API_HASH = DATA["API_HASH"]
    BOT_TOKEN = DATA["BOT_TOKEN"]

# Crear cliente del bot
bot = Client(
    "MY_BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=plugins
)

if __name__ == "__main__":
    # Conectar el bot y obtener detalles
    with bot:
        bot_info = bot.get_me()
        bot_name = bot_info.first_name
        bot_username = bot_info.username

        print(f"Bot on ({bot_name}) - @{bot_username}")
        print("Done Bot Active ✅")
    
    bot.run()
    
