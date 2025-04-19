from aiogram import F, Router
from aiogram.types import Message

from bot.constants import MenuButtons
from bot.keyboards.reply import reply_kb
from bot.utils import send_message_with_keyboard

router = Router(name=__name__)


@router.message(F.text == MenuButtons.SETTINGS.value)
async def settings_commands(message: Message):
    await send_message_with_keyboard(message, "Настройки", reply_kb.settings_menu_btn)
