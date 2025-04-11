import logging
from pathlib import Path
from typing import Optional

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.constants import EXC_MESSAGES
from bot.exceptions import AudioProcessingError, TranscriptionError
from bot.states import TaskCreationStates
from bot.utils import handle_task_creation, request_content_to_llm
from config import settings
from services.transcribe import TranscribeAudio

logger = logging.getLogger(__name__)

router = Router(name="voice_router")


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
            raise AudioProcessingError(EXC_MESSAGES["download_voice"])

    async def transcribe_voice(self, file_path: Path) -> str:
        """Транскрибирование голоса в текст."""
        try:
            return await self.transcriber.transcribe_async(file_path)
        except Exception as e:
            logger.error(f"Ошибка при транскрибировании: {e}")
            raise TranscriptionError(EXC_MESSAGES["transcribe_voice"])

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

    async def process_voice_message(
        self, message: Message, state: FSMContext
    ) -> Optional[str]:
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


@router.message(TaskCreationStates.WAITING_VOICE_INPUT, F.voice)
async def voice_handler(message: Message, state: FSMContext) -> None:
    processor = VoiceMessageProcessor()

    if text := await processor.process_voice_message(message, state):
        await state.update_data(text=text)
        result_text = await request_content_to_llm(text)
        await handle_task_creation(message, state, result_text)
