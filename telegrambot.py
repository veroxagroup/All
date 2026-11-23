from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
import asyncio

from KachoktotiFunksiyalar import kachoktoti_sozlashuvi
from KachoktotiFunksiyalar import qaytaruvchi

dp = Dispatcher()

TOKEN = "8511977347:AAGYCe82E1kqib1-BBNA72bsPiqas9NOGVk"


async def main():
    dp.message.register(kachoktoti_sozlashuvi,CommandStart())

    dp.message.register(qaytaruvchi)

    bot = Bot(token=TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

asyncio.run(main())
