from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import Bot
import requests

from wundbuttons import money_buttons
from wundstate import Tasdiqlash

ADMIN_ID = 8819927088


async def bosganda(bot: Bot):
    await bot.send_message(chat_id=ADMIN_ID,text="Bot ishga tushdi")


async def toxtaganda(bot: Bot):
    await bot.send_message(chat_id=ADMIN_ID,text="Bot ishdan to‘xtadi")


async def start_bosgnada(message: Message):
    await message.answer(f"Assalomu alaykum hurmatli {message.from_user.username}, "f"bu botda siz pul kurslarini topishingiz mumkin.",reply_markup=money_buttons)

async def qiymatli_dollar(message: Message, state:FSMContext):
    await message.answer("Nechi dollar hisoblaymiz?")
    await state.set_state(Tasdiqlash.money)


async def received_qiymatli_dollar(message: Message, state: FSMContext):
    url = "https://v6.exchangerate-api.com/v6/4349ab33d20d7bcd8b3d14da/latest/USD"

    response = requests.get(url)
    data = response.json()

    z = data["conversion_rates"]["UZS"]
    qiymat = float(message.text)

    await message.answer(f"{qiymat} $ == "f"{str(int(qiymat * z))} So'm")

    await state.clear()