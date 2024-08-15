# That's the main file, which you should run to start the bot
# DON'T FORGET TO MODIFY __INIT__.PY FILES AND INSERT TOKEN IN .env

import asyncio
import logging
import os
import time

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from handlers.common import router

start_time = time.time()


async def run_bot():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        # filename="log.txt",           if you want, you can save everything in a file, instead of printing it to the console
    )

    # I just like 'HTML' parse mode, you don't have to use it
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(run_bot())
