from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.commands import Commands
from bot.constants import Messages
from bot.keyboards.reply import reply_kb
from bot.utils import send_message_with_keyboard
from database.repositories import TgProfileRepository

router = Router(name=__name__)


@router.message(Command(Commands.start.name))
async def start_command(message: Message):
    """
    Обработчик команды /start
    """
    tg_id = message.from_user.id

    try:
        # TODO: Вынести в отдельный сервис (UseCase)
        repository = TgProfileRepository()
        user = repository.get_by_tgid(tg_id)
        if not user:
            user = repository.add_new_profile(tg_id)
        await send_message_with_keyboard(
            message, Messages.START.value, reply_kb.menu_btn
        )
    # TODO: Сделать нормальный эксепшен
    except Exception as e:
        await send_message_with_keyboard(message, str(e))


@router.message(Command(Commands.help.name))
async def help_command(message: Message):
    """
    Обработчик команды /help
    """
    await send_message_with_keyboard(message, Messages.HELP.value)


# @router.message(F.text)
# async def echo(message: Message):
#     """
#     Обработчик текстовых сообщений
#     """
#     await send_message_with_keyboard(message, Messages.ECHO.value)
