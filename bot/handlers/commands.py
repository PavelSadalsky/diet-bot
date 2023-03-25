from aiogram.types import Message

from bot.loader import dp


@dp.message_handler(commands=["start"], state="*")
async def start_handler(message: Message):
    await message.answer("Hello!")
