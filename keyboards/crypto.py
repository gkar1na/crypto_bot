import logging
from aiogram import types
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton


logger = logging.getLogger(__name__)


async def get_markup(callback: types.CallbackQuery) -> InlineKeyboardMarkup:
    crypto = [
        ['Bitcoin (BTC)'],
        ['Toncoin (TON)'],
        ['Binance Coin (BNB)'],
        ['Tether (USDT)']
    ]

    buttons = []
    for row in crypto:
        buttons.append([])
        for text in row:
            buttons[-1].append(InlineKeyboardButton(
                text=text,
                callback_data=f'{callback.data}/{(text.split()[-1])}_crpt'
            ))
    buttons.append([InlineKeyboardButton(
        text='< Назад',
        callback_data=callback.data[:callback.data.rfind('/')]
    )])

    markup = InlineKeyboardMarkup()
    for row in buttons:
        markup.row(*row)

    return markup
