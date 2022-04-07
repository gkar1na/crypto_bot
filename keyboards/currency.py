import logging
from aiogram import types
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton


logger = logging.getLogger(__name__)


async def get_markup(callback: types.CallbackQuery) -> InlineKeyboardMarkup:
    currency = [
        ['RUB', 'USD', 'EUR'],
        ['BYN', 'UAH', 'KZT']
    ]

    buttons = []
    for row in currency:
        buttons.append([])
        for text in row:
            buttons[-1].append(InlineKeyboardButton(
                text=text,
                callback_data=f'{callback.data}/{text}_currency'
            ))
    buttons.append([InlineKeyboardButton(
        text='< Назад в Маркет',
        callback_data='welcome'
    )])

    markup = InlineKeyboardMarkup()
    for row in buttons:
        markup.row(*row)

    return markup
