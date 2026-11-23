from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from testbot_states import oyin_rejimi


async def bot_ishga_tushganda(bot: Bot):
    await bot.send_message(
        chat_id=8819927088,
        text="Bot ishga tushdi...."
    )


async def bot_ishdan_toxtaganda(bot: Bot):
    await bot.send_message(
        chat_id=8819927088,
        text="Bot ishdan to'xtadi...."
    )


async def start(message: Message, state: FSMContext):
    await message.answer(
        "Assalomu alaykum! O'yin rejasini tuzamiz.\n"
        "Avval o'yin sanasini yozing!"
    )
    await state.set_state(oyin_rejimi.sana)


async def recived_sana(message: Message, state: FSMContext):
    await state.update_data(sana=message.text)
    await message.answer("O'yin sanasi qabul qilindi. Endi boshlanish vaqtini kiriting!")
    await state.set_state(oyin_rejimi.start_game)


async def recived_start_game(message: Message, state: FSMContext):
    await state.update_data(start_game=message.text)
    await message.answer("Boshlanish vaqti qabul qilindi. Endi o'yin turini kiriting!")
    await state.set_state(oyin_rejimi.game_type)


async def recived_game_type(message: Message, state: FSMContext):
    await state.update_data(game_type=message.text)
    await message.answer("O'yin turi qabul qilindi. Endi manzilni kiriting!")
    await state.set_state(oyin_rejimi.game_location)


async def recived_game_location(message: Message, state: FSMContext):
    await state.update_data(game_location=message.text)
    await message.answer("O'yin joyi qabul qilindi. Endi o'yinchilar sonini kiriting!")
    await state.set_state(oyin_rejimi.players)


async def recived_players(message: Message, state: FSMContext):
    await state.update_data(players=message.text)
    await message.answer("O'yinchilar soni qabul qilindi. Endi jamoa nomini kiriting!")
    await state.set_state(oyin_rejimi.team_name)


async def recived_team_name(message: Message, state: FSMContext):
    await state.update_data(team_name=message.text)
    await message.answer(
        "Jamoa nomi qabul qilindi. Kirish bepulmi? Ha yoki yo'q deb javob bering!"
    )
    await state.set_state(oyin_rejimi.enter_game)


async def recived_enter_game(message: Message, state: FSMContext):
    await state.update_data(enter_game=message.text)
    await message.answer(
        "Javob qabul qilindi. Endi o'yindan keyin qayerga borishni rejalashtiryapsiz?"
    )
    await state.set_state(oyin_rejimi.after_game)


async def recived_after_game(message: Message, state: FSMContext):
    await state.update_data(after_game=message.text)
    await message.answer("O'yindan keyingi reja qabul qilindi. Endi o'yinda musiqa bo'ladimi?")
    await state.set_state(oyin_rejimi.music_in_game)


async def recived_music_in_game(message: Message, state: FSMContext):
    await state.update_data(music_in_game=message.text)
    await message.answer("Javobingiz qabul qilindi. Qo'shimcha izoh yozishingiz mumkin!")
    await state.set_state(oyin_rejimi.izoh)


async def recived_izoh(message: Message, state: FSMContext):
    await state.update_data(izoh=message.text)

    g = await state.get_data()

    text = f"""
O'YIN REJASI

📅 O'yin sanasi: {g.get('sana')}
🕒 Boshlanish vaqti: {g.get('start_game')}
🎮 O'yin turi: {g.get('game_type')}
📍 O'yin joyi: {g.get('game_location')}
👥 Ishtirokchilar soni: {g.get('players')}
🏆 Jamoa nomi: {g.get('team_name')}
🎟 Kirish bepulmi: {g.get('enter_game')}
📌 O'yindan keyingi manzil: {g.get('after_game')}
🎵 O'yinda musiqa bo'ladimi: {g.get('music_in_game')}
📝 Qo'shimcha izoh: {g.get('izoh')}
"""

    await message.answer(text)
    await state.clear()