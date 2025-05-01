# alerts.py

from aiogram import Bot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("ADMIN_CHAT_ID")  # Você pode definir isso no Railway

bot = Bot(token=BOT_TOKEN)

async def send_alert(message):
    if CHAT_ID:
        await bot.send_message(chat_id=CHAT_ID, text=message)
