from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
import asyncio

from testbot_states import oyin_rejimi

from testbot_funcsiyalari import start,bot_ishga_tushganda,bot_ishdan_toxtaganda,recived_sana,recived_start_game,recived_game_type,recived_game_location,recived_players,recived_team_name,recived_enter_game,recived_after_game,recived_music_in_game,recived_izoh

TOKEN = "8885556083:AAHPZVHrK6hTNTwCZui9sP_Eu0cOD5plTYM"

dp = Dispatcher()


async def main():
    dp.startup.register(bot_ishga_tushganda)
    dp.shutdown.register(bot_ishdan_toxtaganda)

    dp.message.register(start, CommandStart())

    dp.message.register(recived_sana, oyin_rejimi.sana)
    dp.message.register(recived_start_game, oyin_rejimi.start_game)
    dp.message.register(recived_game_type, oyin_rejimi.game_type)
    dp.message.register(recived_game_location, oyin_rejimi.game_location)
    dp.message.register(recived_players, oyin_rejimi.players)
    dp.message.register(recived_team_name, oyin_rejimi.team_name)
    dp.message.register(recived_enter_game, oyin_rejimi.enter_game)
    dp.message.register(recived_after_game, oyin_rejimi.after_game)
    dp.message.register(recived_music_in_game, oyin_rejimi.music_in_game)
    dp.message.register(recived_izoh, oyin_rejimi.izoh)

    bot = Bot(TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


asyncio.run(main())