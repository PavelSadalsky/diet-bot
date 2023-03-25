from aiogram.types import Message

from bot.loader import dp


@dp.message_handler(state="*")
async def echo_handler(message: Message):
    await message.answer(message.text)
