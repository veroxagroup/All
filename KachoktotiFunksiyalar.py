from aiogram.types import Message


async def kachoktoti_sozlashuvi(message: Message):
    await message.answer(
        f"🦜 Men ishga tushdim, yozishingiz mumkin {message.from_user.username}!"
    )


async def qaytaruvchi(message: Message):
    await message.answer(message.text)