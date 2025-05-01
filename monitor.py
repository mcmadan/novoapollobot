# monitor.py

import asyncio
from alerts import send_alert

async def monitor_wallets():
    # Simulação para exemplo
    while True:
        await asyncio.sleep(15)  # Aguarda 15 segundos
        await send_alert("🚨 Detecção simulada: carteira X movimentou TOKEN_Y!")
