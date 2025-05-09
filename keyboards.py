from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🆘 Помощь", callback_data="help"),
        InlineKeyboardButton(text="📊 Статус", callback_data="status")
    )
    return builder.as_markup()


def help_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="start"),
        InlineKeyboardButton(text="📊 Статус", callback_data="status")
    )
    return builder.as_markup()


def status_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🆘 Помощь", callback_data="help"),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="start")
    )
    return builder.as_markup()
