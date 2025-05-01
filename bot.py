from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os
import logging
import requests

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("BOT_TOKEN", "8069388714:AAH2PjzKD-D15E8mxbDmeof3dHIsxrZuKjs")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Comando /start
@dp.message_handler(commands=["start"])
async def send_welcome(message: Message):
    await message.reply("Inteligência ativada")

# Comando /price
@dp.message_handler(commands=["price"])
async def crypto_price(message: Message):
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    price = response.json().get("bitcoin", {}).get("usd", "Erro ao obter preço")
    await message.reply(f"💰 Preço do Bitcoin: ${price}")

# Comando /ethprice
@dp.message_handler(commands=["ethprice"])
async def eth_price(message: Message):
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
    price = response.json().get("ethereum", {}).get("usd", "Erro ao obter preço")
    await message.reply(f"💎 Preço do Ethereum: ${price}")

# Comando /gas
@dp.message_handler(commands=["gas"])
async def eth_gas(message: Message):
    response = requests.get("https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=freekey")
    data = response.json().get("result", {})
    gas = data.get("ProposeGasPrice", "Erro ao obter gas")
    await message.reply(f"⛽ Gas da Ethereum: {gas} Gwei")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
