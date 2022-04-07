import logging
from aiogram import types

from config import dp
from keyboards.request import get_markup


logger = logging.getLogger(__name__)
bank_text = '*вставить_текст_для_отправки_к_менеджеру*'


@dp.callback_query_handler(regexp='bank$')
async def send_welcome_callback(callback: types.CallbackQuery):
    logger.info(callback.data)

    await dp.bot.send_message(
        chat_id=callback.from_user.id,
        text=bank_text,
        reply_markup=await get_markup(callback)
    )
