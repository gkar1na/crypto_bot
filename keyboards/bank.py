import logging
from aiogram import types
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton


logger = logging.getLogger(__name__)


async def get_markup(callback: types.CallbackQuery) -> InlineKeyboardMarkup:
    banks = [
        ['Тинькофф'],
        ['СберБанк'],
        ['Альфабанк'],
        ['ВТБ'],
        ['СБП'],
        ['ЮMoney'],
        ['Payeer']
    ]

    buttons = []
    for row in banks:
        buttons.append([])
        for text in row:
            buttons[-1].append(InlineKeyboardButton(
                text=text,
                callback_data=f'{callback.data}/{text}_bank'
            ))
    buttons.append([InlineKeyboardButton(
        text='< Назад',
        callback_data=callback.data[:callback.data.rfind('/')]
    )])

    markup = InlineKeyboardMarkup()
    for row in buttons:
        markup.row(*row)

    return markup
