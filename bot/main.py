# That's the main file, which you should run to start the bot
# DON'T FORGET TO MODIFY __INIT__.PY FILES AND INSERT TOKEN IN .env

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from handlers import common


async def run_bot():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename="log.txt",
    )

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))  # I just like 'HTML' parse mode, you can use another one
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(common.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(run_bot())
