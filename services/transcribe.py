import asyncio
import logging
import threading
from pathlib import Path

import whisper

from config import settings

logger = logging.getLogger(__name__)


class TranscribeAudio:
    VALID_FORMATS = (".ogg", ".wav", ".mp3")

    def __init__(self):
        self.lock = threading.Lock()
        self.model = None
        self._initialize_model()

    def _initialize_model(self):
        # Инициализация модели распознования речи
        try:
            self.model = whisper.load_model(
                settings.model_name,
                device="cpu",
                download_root=settings.models_path,
            )
        except Exception as e:
            logger.error(f"Ошибка инициализации модели: {str(e)}")
            raise

    async def transcribe_async(self, file_path: Path) -> str:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._transcribe_sync, file_path)

    def _transcribe_sync(self, file_path: Path) -> str:
        with self.lock:
            try:
                self._validate_file(file_path)
                result = self.model.transcribe(str(file_path), fp16=False)
                return result["text"].strip()
            except Exception as e:
                logger.error(f"Ошибка транскрибации: {str(e)}")
                raise

    def _validate_file(self, file_path: Path):
        """Проверка файла."""
        if not file_path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        if file_path.suffix.lower() not in self.VALID_FORMATS:
            raise ValueError(f"Недопустимый формат файла: {file_path.suffix}")

    def __del__(self):
        """Очистка ресурсов."""
        del self.model
