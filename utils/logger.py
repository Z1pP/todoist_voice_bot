import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging(logs_dir: str = "logs/"):
    # Создание папки для логов
    os.makedirs(logs_dir, exist_ok=True)
    # Основные настройки
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Логирование в файл
    file_handler = RotatingFileHandler(
        f"{logs_dir}app.log",
        maxBytes=5 * 1024 * 1024,  # 5MB
        backupCount=5,  # Сохраняем 5 старых логов
    )
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    logging.getLogger().addHandler(file_handler)

    # Логирование ошибок в отдельный файл
    error_handler = RotatingFileHandler(
        f"{logs_dir}error.log", maxBytes=5 * 1024 * 1024, backupCount=5
    )
    error_handler.setLevel(logging.ERROR)
    error_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    error_handler.setFormatter(error_formatter)
    logging.getLogger().addHandler(error_handler)
