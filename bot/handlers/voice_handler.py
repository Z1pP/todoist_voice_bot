import logging
from pathlib import Path
from typing import Optional

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.constants import ExceptionMessages
from bot.exceptions import AudioProcessingError, TranscriptionError
from bot.handlers.task_handler import proccess_llm_processing
from bot.states import TaskCreationStates
from config import settings
from services.transcribe import TranscribeAudio

logger = logging.getLogger(__name__)

router = Router(name=__name__)


class VoiceMessageHandler:
    """
    Класс для обработки голосовых сообщений
    """

    def __init__(self, transcriber: TranscribeAudio):
        self.transcriber = transcriber
        self.voice_dir = Path(settings.voice_dir)
        self._create_voice_directory()

    def _create_voice_directory(self) -> None:
        # Если папки нет, создаем её
        self.voice_dir.mkdir(parents=True, exist_ok=True)

    def _get_file_path(self, file_id: str) -> Path:
        return self.voice_dir / f"{file_id}.ogg"

    async def download_voice(self, message: Message, file_path: Path) -> None:
        """
        Скачивание голосового сообщения по file_id.
        """
        try:
            await message.bot.download(message.voice.file_id, destination=file_path)
        except Exception as e:
            logger.error(f"Ошибка при загрузке файла: {str(e)}")
            raise AudioProcessingError(ExceptionMessages.DOWNLOAD_VOICE.value)

    async def transcribe_voice(self, file_path: Path) -> str:
        """Транскрибирование голоса в текст."""
        try:
            return await self.transcriber.transcribe_async(file_path)
        except Exception as e:
            logger.error(f"Ошибка при транскрибировании: {e}")
            raise TranscriptionError(ExceptionMessages.TRANSCRIBE_VOICE.value)

    def cleanup_file(self, file_path: Path) -> None:
        """Удаление временных файлов."""
        try:
            if file_path.exists():
                file_path.unlink()
        except Exception as e:
            logger.warning(f"Ошибка при удалении времпнного файла {file_path}: {e}")


class VoiceMessageProcessor:
    def __init__(self):
        self.handler = VoiceMessageHandler(TranscribeAudio())

    async def process_voice_message(self, message: Message) -> Optional[str]:
        file_path = self.handler._get_file_path(message.voice.file_id)

        try:
            await self.handler.download_voice(message, file_path)
            text = await self.handler.transcribe_voice(file_path)

            logger.info(f"Успешно транскрибирован файл {message.voice.file_id}")
            return text

        except (AudioProcessingError, TranscriptionError) as e:
            await message.reply(str(e))
            logger.error(f"Ошибка при транскрибировании: {e}")
            return None

        finally:
            self.handler.cleanup_file(file_path)


@router.message(TaskCreationStates.WAINTING_INPUT, F.voice)
async def proccess_voice_input(message: Message, state: FSMContext):
    voice_processor = VoiceMessageProcessor()

    if text := await voice_processor.process_voice_message(message):
        await proccess_llm_processing(message, state, text)
