from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from registerstate import Regestrationstate


foydalanuvchilar = []


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


async def start_register(message: Message):
    await message.answer("Assalomu alaykum!")


async def help_register(message: Message, state: FSMContext):
    await message.answer("Ismingizni kiriting.")
    await state.set_state(Regestrationstate.ism)


async def recived_ism(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)

    await message.answer("Ismingiz qabul qilindi. Familyangizni kiriting.")
    await state.set_state(Regestrationstate.familya)


async def recived_familya(message: Message, state: FSMContext):
    await state.update_data(familya=message.text)

    await message.answer("Familyangiz qabul qilindi. Telefon raqamingizni kiriting.")
    await state.set_state(Regestrationstate.tel_raqam)


async def recived_tel_raqam(message: Message, state: FSMContext):
    await state.update_data(tel_raqam=message.text)

    g = await state.get_data()

    text = f"""
Ma'lumotlaringiz qabul qilindi!

Ismingiz: {g.get('ism')}
Familyangiz: {g.get('familya')}
Telefon raqamingiz: {g.get('tel_raqam')}
"""

    await message.answer(text)
    await message.answer("Ma'lumotlaringiz to'g'rimi?")

    await state.set_state(Regestrationstate.tasdiqlash)


async def tasdiqlash(message: Message, state: FSMContext):

    if message.text.lower() == "ha":

        g = await state.get_data()

        foydalanuvchilar.append(g)

        await message.answer("Ro'yxatdan muvaffaqiyatli o'tdingiz!")
        print(foydalanuvchilar)

        await state.clear()

    else:
        await message.answer("Ma'lumotlar noto'g'ri. Qaytadan ismingizni kiriting.")

        await state.clear()
        await state.set_state(Regestrationstate.ism)