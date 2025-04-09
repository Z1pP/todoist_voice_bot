import logging
import os
from pathlib import Path

from aiogram import F, Router
from aiogram.types import Message

from config import settings
from services.transcribe import TranscribeAudio

logger = logging.getLogger(__name__)

router = Router(name="voice_router")


@router.message(F.voice)
async def voice_handler(message: Message):
    file_id = message.voice.file_id
    file_name = f"{file_id}.ogg"
    file_path = Path(os.path.join(settings.voice_dir, file_name))

    try:
        # Загрузка файла
        await message.bot.download(file_id, destination=file_path)
        # Транскрибация
        transcb = TranscribeAudio()

        text = await transcb.transcribe_async(file_path)

        await message.answer("Обработка завершена!")
        await message.reply(text)

        logger.info(f"Транскрибация успешна для {file_id}")
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден")
        await message.reply("Файл не найден.")
    except Exception as e:
        logger.error(f"Ошибка: {str(e)}")
        await message.reply("Произошла ошибка при обработке.")
    finally:
        # Удаление файла после обработки
        if os.path.exists(file_path):
            os.remove(file_path)
