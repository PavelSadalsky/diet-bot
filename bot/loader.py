from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils import Config

config = Config.load()
memory_storage = MemoryStorage()
bot = Bot(token=config.bot_token, parse_mode="HTML")
dp = Dispatcher(bot, storage=memory_storage)
