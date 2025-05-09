from aiogram import types


def get_start_text(user: types.User) -> str:
    return (
        f"Привет, {user.full_name}!\n"
        f"ID: {user.id}\n"
        f"Username: @{user.username}\n\n"
        "Я простой бот с базовыми командами.\n"
        "Используй меню или кнопки ниже."
    )


def get_help_text() -> str:
    return (
        "📚 Справочная информация:\n\n"
        "/start - Запуск бота\n"
        "/help - Справка\n"
        "/status - Информация о пользователе\n\n"
        "Бот отвечает эхом на текстовые сообщения."
    )


def get_status_text(user: types.User) -> str:
    text = (
        "👤 Информация:\n\n"
        f"🆔 ID: {user.id}\n"
        f"📛 Username: @{user.username}\n"
        f"👀 Имя: {user.first_name}"
    )
    return text + f" {user.last_name}" if user.last_name else text
