from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from container import container
from core.application.use_cases.user_use_cases import GetOrCreateUserUseCase
from presentation.constants.bot_constants import Messages
from presentation.keyboards import reply_kb
from utils import send_message_with_keyboard

router = Router(name=__name__)


@router.message(Command("start"))
async def start_handler(msg: Message):
    usecase: GetOrCreateUserUseCase = container.resolve(GetOrCreateUserUseCase)
    _ = await usecase.execute(tg_id=msg.from_user.id, username=msg.from_user.username)

    await send_message_with_keyboard(msg, Messages.Dialog.MENU, reply_kb.menu_btn)


@router.message(Command("help"))
async def help_handler(msg: Message):
    await msg.answer(Messages.Dialog.HELP)
