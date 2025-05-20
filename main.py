import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from callbacks import callback_router
from config import TOKEN

from answers import get_help_text, get_start_text, get_status_text
from keyboards import start_keyboard, help_keyboard, status_keyboard
from logger import setup_logging

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(callback_router)

setup_logging()


async def set_bot_commands():
    commands = [
        types.BotCommand(command="start", description="Запуск бота"),
        types.BotCommand(command="help", description="Справка по командам"),
        types.BotCommand(command="status", description="Информация о пользователе"),
    ]
    await bot.set_my_commands(commands)


@dp.message(Command("start"))
async def process_start_command(message: types.Message):
    user = message.from_user

    logging.info(
        f"User - @{user.username} ввел(а) /start"
    )

    await message.answer(
        text=get_start_text(user=user),
        reply_markup=start_keyboard()
    )


@dp.message(Command("help"))
async def process_help_command(message: types.Message):
    logging.info(
        f"User - @{message.from_user.username} ввел(а) /help"
    )

    await message.answer(
        text=get_help_text(),
        reply_markup=help_keyboard()
    )


@dp.message(Command("status"))
async def process_status_command(message: types.Message):
    user = message.from_user

    logging.info(
        f"User - @{user.username} ввел(а) /status"
    )

    await message.answer(
        text=get_status_text(user=user),
        reply_markup=status_keyboard()
    )


@dp.message()
async def echo_message(message: types.Message):
    logging.info(
        f"User - @{message.from_user.username} написал(а) {message.text}"
    )

    await message.answer(message.text)


async def main():
    await set_bot_commands()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
