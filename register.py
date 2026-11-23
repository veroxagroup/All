import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command

import registerfunction
from registerstate import Regestrationstate


TOKEN = "8788531890:AAEci4D6isQndFv75riUPz3bAhgS4cuwDN8"

dp = Dispatcher()


async def main():

    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp.startup.register(registerfunction.bot_ishga_tushganda)
    dp.shutdown.register(registerfunction.bot_ishdan_toxtaganda)

    dp.message.register(registerfunction.start_register, CommandStart())

    dp.message.register(registerfunction.help_register, Command("help"))

    dp.message.register(registerfunction.recived_ism, Regestrationstate.ism)

    dp.message.register(registerfunction.recived_familya, Regestrationstate.familya)

    dp.message.register(registerfunction.recived_tel_raqam, Regestrationstate.tel_raqam)

    dp.message.register(registerfunction.tasdiqlash, Regestrationstate.tasdiqlash)

    await dp.start_polling(bot)


asyncio.run(main())