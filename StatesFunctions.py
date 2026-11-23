from aiogram.types import Message, message_entity, reply_keyboard_markup
from aiogram import Bot
from aiogram import html
from StatesShablomn import IshJoyiKerakState
from aiogram.fsm.context import FSMContext
from outline_buttons import confrim_buttons
async def bot_ishga_tushganda(bot:Bot):
    await bot.send_message(chat_id=8819927088, text="Bot ishga tushdi...")


async def bot_ishdan_toxtaganda(bot:Bot):
    await bot.send_message(chat_id=8819927088, text="Bot ishdan toxtadi...")


async def start_bosganda(message:Message, state:FSMContext):
    matn = """Ish joyi topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi."""

    await message.answer(matn,reply_markup=confrim_buttons)
    await message.answer(html.bold("Ism, familyangizni kiriting?"))
    await state.set_state(IshJoyiKerakState.ism_familya)

async def full_name_received(message:Message, state:FSMContext):
    await state.update_data(ism_familya=message.text)
    await message.answer("""🕑 Yosh: 

Yoshingizni kiriting?""")
    await state.set_state(IshJoyiKerakState.yosh)

async def yosh(message:Message, state:FSMContext):
    await state.update_data(yosh=message.text)
    x = """📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
"""
    await message.answer(x)
    await state.set_state(IshJoyiKerakState.texnologiya)

async def texnologiya(message:Message, state:FSMContext):
    await state.update_data(texnologiya=message.text)
    y = """📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?"""
    await message.answer(y)
    await state.set_state(IshJoyiKerakState.telefon_raqam)

async def tel_raqam(message:Message, state:FSMContext):
    await state.update_data(tel_raqam=message.text)
    h = """🌐 Hudud: 

Qaysi hududdansiz?
"""

    await message.answer(h)
    await state.set_state(IshJoyiKerakState.hudud)

async def hudud(message:Message, state:FSMContext):
    await state.update_data(hudud=message.text)
    n = """💰 Narxi:

Tolov istaysizmi yoki Tekinmi?
Agar istasangiz, Summani kiriting?"""
    await message.answer(n)
    await state.set_state(IshJoyiKerakState.narxi)

async def narxi(message:Message, state:FSMContext):
    await state.update_data(narxi=message.text)
    k = """👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?"""
    await message.answer(k)
    await state.set_state(IshJoyiKerakState.kasbi)

async def kasbi(message:Message, state:FSMContext):
    await state.update_data(kasbi=message.text)
    m = """🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?"""
    await message.answer(m)
    await state.set_state(IshJoyiKerakState.vaqti)

async def murojaat(message:Message, state:FSMContext):
    await state.update_data(murojaat=message.text)
    maqsad = """🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering."""
    await message.answer(maqsad)
    await state.set_state(IshJoyiKerakState.maqsad)

async def maqsad(message:Message, state:FSMContext):
    await state.update_data(maqsad=message.text)

    d = await state.get_data()

    text = f"""Ish joyi kerak:

👨‍💼 Xodim: {d.get('ism_familya')}
🕑 Yosh: {d.get('yosh')}
📚 Texnologiya: {d.get('texnologiya')}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {d.get('tel_raqam')}
🌐 Hudud: {d.get('hudud')}
💰 Narxi: {d.get('narxi')}
👨‍💻 Kasbi: {d.get('kasbi')}
⏰ Murojaat qilish vaqti: {d.get('murojaat')}
🔎 Maqsad: {d.get('maqsad')}"""

    await message.answer(text)
    await message.answer("Barcha malumotlar togrimi")
    await state.set_state(IshJoyiKerakState.tasdiqlash)

async def tasdiqlash_p(message: Message , bot: Bot, state: FSMContext):
    if message.text.lower() == 'ha':
        d = await state.get_data()

        text = f"""Ish joyi kerak:
    
        👨‍💼 Xodim: {d.get('ism_familya')}
        🕑 Yosh: {d.get('yosh')}
        📚 Texnologiya: {d.get('texnologiya')}
        🇺🇿 Telegram: @{message.from_user.username}
        📞 Aloqa: {d.get('tel_raqam')}
        🌐 Hudud: {d.get('hudud')}
        💰 Narxi: {d.get('narxi')}
        👨‍💻 Kasbi: {d.get('kasbi')}
        ⏰ Murojaat qilish vaqti: {d.get('murojaat')}
        🔎 Maqsad: {d.get('maqsad')}"""

        await bot.send_message(chat_id=8819927088, text = text)
        await message.answer("Elon adminga jonatildi 24 soat ichida korib chiqiladi")
        await state.clear()
    else:
        await message.answer("Arizangiz bekor qilindi")






















