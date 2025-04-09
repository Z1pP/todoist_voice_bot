import asyncio
import logging
import os
import threading
from typing import Optional

import whisper

from config import settings

logger = logging.getLogger(__name__)


class TranscribeAudio:
    def __init__(self):
        self.__create_folder_for_models()
        self.model = whisper.load_model(
            name=settings.model_name,
            download_root=settings.models_path,
            device="cpu",
        )
        self.lock = threading.Lock()

    def __create_folder_for_models(self):
        if not os.path.exists(settings.models_path):
            os.makedirs(settings.models_path)

    async def transcribe_async(
        self, file_path: str, language: Optional[str] = None
    ) -> str:
        # Асинхронная обработка через потоки
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None, lambda: self._transcribe_sync(file_path, language)
        )

    def _transcribe_sync(self, file_path: str, language: Optional[str] = None) -> str:
        """Синхронный метод транскрибации."""
        with self.lock:
            try:
                options = {"language": language} if language else {}
                result = self.model.transcribe(file_path, **options)
                return result["text"].strip()
            except Exception as e:
                logger.error(f"Ошибка транскрибации: {str(e)}")
                raise e

    @staticmethod
    def validate_file(file_path: str):
        """Проверка существования файла и расширения."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не найден")
        if not file_path.lower().endswith((".ogg", ".wav")):
            raise ValueError("Неподдерживаемый формат файла")
