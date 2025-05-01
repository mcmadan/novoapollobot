# bot.py

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import logging
import asyncio
import os
from monitor import monitor_wallets

API_TOKEN = os.getenv("BOT_TOKEN", "8069388714:AAH2PjzKD-D15E8mxbDmeof3dHIsxrZuKjs")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: Message):
    await message.reply("Inteligência ativada")

@dp.message_handler(commands=["status"])
async def status(message: Message):
    await message.reply("Apollo 1.5 está online e monitorando...")

async def on_startup(_):
    asyncio.create_task(monitor_wallets())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
