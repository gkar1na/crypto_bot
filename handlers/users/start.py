import logging
from aiogram import types

from config import dp
from keyboards.welcome import get_markup


logger = logging.getLogger(__name__)
welcome_text = '*вставить_приветственный_текст*'


@dp.message_handler(commands=['start'])
async def send_welcome_command(message: types.Message):
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text=welcome_text,
        reply_markup=await get_markup()
    )


@dp.callback_query_handler(text=['welcome'])
async def send_welcome_callback(callback: types.CallbackQuery):
    logger.info(callback.data)

    await dp.bot.send_message(
        chat_id=callback.from_user.id,
        text=welcome_text,
        reply_markup=await get_markup()
    )
