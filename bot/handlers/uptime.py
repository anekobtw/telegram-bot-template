import time

from aiogram import F, types
from aiogram.filters import Command
from common import router

from main import start_time


@router.message(F.text, Command("uptime"))
async def uptime(message: types.Message) -> None:
    await message.answer(f"Status: {round(time.time() - start_time)} seconds")
