# If you want to, create keyboards here

from aiogram import types


def get_start_kb() -> types.ReplyKeyboardMarkup:
    buttons = [
        ["Example 1", "Example 2"],  # it's the first row
        ["Example 3", "Example 4"],  # it's the second row
    ]

    return types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text=btn) for btn in row] for row in buttons],
        resize_keyboard=True,
        input_field_placeholder="Choose an action",
    )
