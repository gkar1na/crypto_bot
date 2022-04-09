import logging
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton


logger = logging.getLogger(__name__)


async def get_markup() -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(
            text='Купить',
            callback_data=f's/buy'
        ),
        InlineKeyboardButton(
            text='Продать',
            callback_data=f's/sell'
        )
    ]

    markup = InlineKeyboardMarkup()
    markup.row(
        buttons[0], buttons[1]
    )

    return markup
