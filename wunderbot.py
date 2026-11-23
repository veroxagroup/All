from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
from aiogram.filters import Command, CommandStart

from wunderfunc import toxtaganda,bosganda,start_bosgnada,qiymatli_dollar,received_qiymatli_dollar


from wundstate import Tasdiqlash


TOKEN = "8885556083:AAHPZVHrK6hTNTwCZui9sP_Eu0cOD5plTYM"

dp = Dispatcher()


async def main():
    dp.startup.register(bosganda)

    dp.message.register(start_bosgnada, CommandStart())
    dp.message.register(qiymatli_dollar, Command("Dollar_kursi"))
    dp.message.register(received_qiymatli_dollar, Tasdiqlash.money)

    dp.shutdown.register(toxtaganda)

    bot = Bot(TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


asyncio.run(main())