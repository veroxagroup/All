from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


money_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text="/Dollar_kursi")
        ]
    ],
    resize_keyboard=True
)