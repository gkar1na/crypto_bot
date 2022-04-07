import logging
from aiogram import types

from config import dp
from keyboards.bank import get_markup


logger = logging.getLogger(__name__)
bank_text = '*вставить_текст_к_выбору_банка*'


@dp.callback_query_handler(regexp='currency$')
async def send_welcome_callback(callback: types.CallbackQuery):
    logger.info(callback.data)

    await dp.bot.send_message(
        chat_id=callback.from_user.id,
        text=bank_text,
        reply_markup=await get_markup(callback)
    )
