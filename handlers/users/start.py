import logging
from aiogram import types

from config import dp
from keyboards.welcome import get_markup


logger = logging.getLogger(__name__)

welcome_text = '''
💠 Здесь вы можете купить или продать криптовалюту с помощью перевода на карту или электронный кошелёк.
🛡 Бот выступает гарантом и удерживает монеты на время сделки.
'''


@dp.message_handler(commands=['start'])
async def send_welcome_command(message: types.Message):
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text=welcome_text,
        reply_markup=await get_markup()
    )


@dp.callback_query_handler(text=['s'])
async def send_welcome_callback(callback: types.CallbackQuery):
    try:
        await dp.bot.delete_message(callback.from_user.id, callback.message.message_id)
    except Exception as e:
        logger.error(e)

    await dp.bot.send_message(
        chat_id=callback.from_user.id,
        text=welcome_text,
        reply_markup=await get_markup()
    )
