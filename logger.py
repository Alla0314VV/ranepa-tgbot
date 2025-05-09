import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path


def setup_logging():
    # Создание папки для логов если ее нет
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Формат логов
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Основной логгер
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Файловый обработчик с ежедневной ротацией
    file_handler = TimedRotatingFileHandler(
        filename=log_dir / 'bot.log',
        when='midnight',
        backupCount=7,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    # Консольный вывод
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Обработчики
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Логирование aiogram
    logging.getLogger('aiogram').setLevel(logging.INFO)
