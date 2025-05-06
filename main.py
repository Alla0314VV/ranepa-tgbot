import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import TOKEN

# Экземпляры бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()


# Устанавливаем меню команд (отображается в интерфейсе Telegram)
async def set_bot_commands():
    commands = [
        types.BotCommand(command="start", description="Запуск бота"),
        types.BotCommand(command="help", description="Справка по командам"),
        types.BotCommand(command="status", description="Информация о пользователе"),
    ]
    await bot.set_my_commands(commands)


@dp.message(Command("start"))
async def process_start_command(message: types.Message):
    user_info = (
        f"Привет, {message.from_user.full_name}!\n"
        f"ID: {message.from_user.id}\n"
        f"Username: @{message.from_user.username}\n\n"
        f"Я простой бот с базовыми командами.\n"
        f"Используй меню команд или вводи их вручную."
    )
    await message.answer(user_info)


@dp.message(Command("help"))
async def process_help_command(message: types.Message):
    help_text = (
        "📚 Справочная информация:\n\n"
        "/start - Запуск бота и информация о пользователе\n"
        "/help - Справка по командам\n"
        "/status - Информация о пользователе (ID и username)\n\n"
        "Бот также отвечает эхом на любое текстовое сообщение."
    )
    await message.answer(help_text)


@dp.message(Command("status"))
async def process_status_command(message: types.Message):
    status_text = (
        "👤 Информация о пользователе:\n\n"
        f"🆔 ID: {message.from_user.id}\n"
        f"📛 Username: @{message.from_user.username}\n"
        f"👀 Имя: {message.from_user.first_name}"
    )
    if message.from_user.last_name:
        status_text += f" {message.from_user.last_name}"
    await message.answer(status_text)


# Эхо-ответ на любое сообщение
@dp.message()
async def echo_message(message: types.Message):
    await message.answer(message.text)


async def main():
    await set_bot_commands()  # Устанавливаем меню команд
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
