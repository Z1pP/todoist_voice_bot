from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.constants import MESSAGES
from bot.keyboards.reply import reply_kb
from bot.utils import send_message_with_keyboard

router = Router(name=__name__)


@router.message(Command("start"))
async def start_command(message: Message):
    """
    Обработчик команды /start
    """
    await send_message_with_keyboard(message, MESSAGES["start"], reply_kb.menu)


@router.message(Command("help"))
async def help_command(message: Message):
    """
    Обработчик команды /help
    """
    await send_message_with_keyboard(message, MESSAGES["help"])
