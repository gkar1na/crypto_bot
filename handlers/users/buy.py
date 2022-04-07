import logging
from aiogram import types

from config import dp
from keyboards.currency import get_markup


logger = logging.getLogger(__name__)
buy_text = '*вставить_текст_к_выбору_валюты_для_покупки*'


@dp.callback_query_handler(regexp='buy$')
async def send_welcome_callback(callback: types.CallbackQuery):
    logger.info(callback.data)

    await dp.bot.send_message(
        chat_id=callback.from_user.id,
        text=buy_text,
        reply_markup=await get_markup(callback)
    )
