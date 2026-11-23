from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



confrim_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(callback_data='x',text="Sherik kerak"),
            InlineKeyboardButton(callback_data='y',text="Ish joy kerak"),


        ],
        [
            InlineKeyboardButton(callback_data='o',text="Xodim kerak"),
            InlineKeyboardButton(callback_data='p',text="Ustoz kerak"),
        ],
        [
            InlineKeyboardButton(callback_data='m',text="Shogirt kerak")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Iltimos xabar yozing...",
    one_time_keyboard=True

)
