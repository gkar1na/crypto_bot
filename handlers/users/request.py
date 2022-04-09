import logging
from aiogram import types

from config import dp
from keyboards.request import get_markup


logger = logging.getLogger(__name__)
final_text = '''
⚠️ Ознакомьтесь с правилами ниже и подтвердите своё согласие.

1. Будьте вежливы. На сделки и сообщения в боте отвечают реальные люди. Соблюдайте условия сделки и правила делового общения.

2. Будьте внимательны. Оплата должна быть отправлена только через выбранный способ оплаты. Отправляйте точную сумму оплаты, указанную в сделке.

3. Будьте уверены. Убедитесь, что вы можете отправить или принять оплату. После получения или отправки реквизитов сделка не может быть отменена.
'''


@dp.callback_query_handler(regexp='bank$')
async def send_welcome_callback(callback: types.CallbackQuery):
    try:
        await dp.bot.delete_message(callback.from_user.id, callback.message.message_id)
    except Exception as e:
        logger.error(e)

    await dp.bot.send_message(
        chat_id=callback.from_user.id,
        text=final_text,
        reply_markup=await get_markup(callback)
    )
