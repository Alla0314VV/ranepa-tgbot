from aiogram import F, Router
from aiogram.types import CallbackQuery

from answers import get_help_text, get_start_text, get_status_text
from keyboards import start_keyboard, help_keyboard, status_keyboard

callback_router = Router()


@callback_router.callback_query(F.data == "start")
async def handle_start(callback: CallbackQuery):
    user = callback.from_user

    await callback.message.edit_text(
        text=get_start_text(user=user),
        reply_markup=start_keyboard()
    )
    await callback.answer()


@callback_router.callback_query(F.data == "help")
async def handle_help(callback: CallbackQuery):
    await callback.message.edit_text(
        text=get_help_text(),
        reply_markup=help_keyboard()
    )
    await callback.answer()


@callback_router.callback_query(F.data == "status")
async def handle_status(callback: CallbackQuery):
    user = callback.from_user

    await callback.message.edit_text(
        text=get_status_text(user=user),
        reply_markup=status_keyboard()
    )
    await callback.answer()
