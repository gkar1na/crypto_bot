import logging
from aiogram import types
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

from config import settings, dp

logger = logging.getLogger(__name__)

url = 't.me'


async def get_markup(callback: types.CallbackQuery) -> InlineKeyboardMarkup:
    admin_number = randint(0, len(settings.ADMINS_ID) - 1)
    admin_id = settings.ADMINS_ID[admin_number]
    admin_username = settings.ADMINS_USERNAME[admin_number]

    await dp.bot.send_message(
        chat_id=admin_id,
        text=f'Новый пользователь: @{callback.from_user.username}:\n'
             f'id: {callback.from_user.id}\n'
             f'Имя: {callback.from_user.first_name}\n'
             f'Фамилия: {callback.from_user.last_name}\n\n'
             f'Запрос: {callback.data}'
    )

    buttons = [
        InlineKeyboardButton(
            text='Начнём >',
            callback_data=f'{callback.data}/{admin_id}_final',
            url=f'{url}/{admin_username}'
        )
    ]

    markup = InlineKeyboardMarkup()
    for button in buttons:
        markup.add(button)

    return markup
