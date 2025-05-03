from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.commands import Commands
from bot.constants import Messages
from bot.exceptions import BotBaseException
from bot.keyboards.reply import reply_kb
from bot.services import UserService
from bot.utils import send_message_with_keyboard

router = Router(name=__name__)


"""
Хэндлеры:
1. Создать задание
2. Посмотреть список заданий
3. Статистика
4. Настройки
5. Помощь
"""


@router.message(Command(Commands.start.name))
async def start_command(message: Message):
    """
    Отображает кнопки главного меню
    """
    try:
        service = UserService()
        _ = service.get_or_create_user(tg_id=message.from_user.id)
        await send_message_with_keyboard(
            message, Messages.Dialog.START, reply_kb.menu_btn
        )
    except BotBaseException as e:
        await send_message_with_keyboard(
            message, str(e.user_message), reply_kb.menu_btn
        )
