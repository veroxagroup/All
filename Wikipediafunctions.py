import wikipedia
from aiogram.types import Message

wikipedia.set_lang("uz")


async def start_wiki(message: Message):
    await message.answer(
        "Assalomu alaykum!\n"
        "Menga istalgan mavzuni yozing va men sizga malumotlar beraman🥸"
    )


async def wikipedia_search(message: Message):
    result = wikipedia.summary(message.text, sentences=50)

    await message.answer(result)