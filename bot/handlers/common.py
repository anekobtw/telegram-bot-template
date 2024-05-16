# Write function handers here, examples are provided below

from aiogram import F, Router, types
from aiogram.filters import Command
from keyboards import get_start_kb
from main import router


# Simple start command
@router.message(F.text, Command("start"))
async def start_command_handler(message: types.Message) -> None:
    keyboard = get_start_kb()
    await message.answer(text="Hi, how are you?", reply_markup=keyboard)


# Let's try to process the message from the buttons
# Keep in mind that I'm checking the text on the button, but it's advisable to check the F.data of a button
@router.message(F.text.in_(["Example 1", "Example 2"]))
async def example_row1_handler(message: types.Message) -> None:
    await message.answer(text="You pressed a button in the first row.")


@router.message(F.text.in_(["Example 3", "Example 4"]))
async def example_row2_handler(message: types.Message) -> None:
    await message.answer(text="You pressed a button in the second row.")
