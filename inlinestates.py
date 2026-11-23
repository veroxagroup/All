from aiogram.types import CallbackQuery

from StatesShablomn import IshJoyiKerakState

async def pressed_ishjoy(callback:CallbackQuery):
    await callback.message.answer(IshJoyiKerakState.ism_familya)