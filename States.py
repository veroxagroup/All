import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from StatesShablomn import IshJoyiKerakState
import inlinestates

import StatesFunctions
dp = Dispatcher()
TOKEN = "8897894611:AAFX4y-ppwtbQlKpvKvI0D4dfXnsZ2l0Guc"


async def main():
    dp.callback_query.register(inlinestates.pressed_ishjoy, F.data=='y')
    dp.startup.register(StatesFunctions.bot_ishga_tushganda)
    dp.message.register(StatesFunctions.start_bosganda, CommandStart())
    dp.message.register(StatesFunctions.full_name_received, IshJoyiKerakState.ism_familya)
    dp.message.register(StatesFunctions.yosh, IshJoyiKerakState.yosh)
    dp.message.register(StatesFunctions.texnologiya, IshJoyiKerakState.texnologiya)
    dp.message.register(StatesFunctions.tel_raqam, IshJoyiKerakState.telefon_raqam)
    dp.message.register(StatesFunctions.hudud, IshJoyiKerakState.hudud)
    dp.message.register(StatesFunctions.narxi, IshJoyiKerakState.narxi)
    dp.message.register(StatesFunctions.kasbi, IshJoyiKerakState.kasbi)
    dp.message.register(StatesFunctions.murojaat, IshJoyiKerakState.vaqti)
    dp.message.register(StatesFunctions.maqsad, IshJoyiKerakState.maqsad)
    dp.shutdown.register(StatesFunctions.bot_ishdan_toxtaganda)
    bot = Bot(token=TOKEN, default=DefaultBotProperties (parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)



asyncio.run(main())