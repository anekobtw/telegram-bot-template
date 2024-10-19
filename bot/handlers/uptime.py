import time

from aiogram import F, types, Router
from aiogram.filters import Command

from main import start_time

router = Router()


@router.message(F.text, Command("uptime"))
async def uptime(message: types.Message) -> None:
    await message.answer(f"Uptime: {round(time.time() - start_time)} seconds")
