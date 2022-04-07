from typing import Optional

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pydantic import BaseSettings
from aiogram.types import ParseMode

from aiogram import Dispatcher, Bot, types


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Crypto Bot'
    TG_TOKEN: Optional[str]
    ADMINS_ID: list = []
    ADMINS_USERNAME: list = []

    class Config:
        env_prefix = ''
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()

storage = MemoryStorage()
bot = Bot(token=settings.TG_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
