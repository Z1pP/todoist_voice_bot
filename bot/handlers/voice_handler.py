import os

from aiogram import F, Router
from aiogram.types import Message

from config import settings

router = Router(name="voice_router")


@router.message(F.voice)
async def voice_handler(message: Message):
    file_id = message.voice.file_id
    file_path = os.path.join(settings.voice_dir, f"{file_id}.ogg")

    try:
        await message.bot.download(file_id, file_path)
        await message.reply("Обработка завершена!")
    except Exception as e:
        await message.reply(f"Ошибка: {str(e)}")
