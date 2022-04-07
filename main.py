import logging
from aiogram import executor
import handlers
from utils.set_bot_commands import set_default_commands
from config import dp


logging.basicConfig(level=logging.INFO)


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
