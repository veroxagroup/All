import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from Wikipediafunctions import start_wiki, wikipedia_search


TOKEN = "8371075102:AAHvjZHJubaIaSz_NohEjbVD45yZ823HU38"

bot = Bot(TOKEN)
dp = Dispatcher()


dp.message.register(start_wiki, Command("start"))
dp.message.register(wikipedia_search)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())