from aiogram import F, Router
from aiogram.types import Message

from presentation.constants.bot_constants import MenuButtons
from presentation.keyboards import reply_kb
from utils import send_message_with_keyboard

router = Router(name=__name__)

MENU_BUTTONS_VALUEST = [button.value for button in MenuButtons]


# @router.message(F.text.in_(MENU_BUTTONS_VALUEST))
# async def menu_handler(msg: Message):
#     text = f" Ты выбрал {msg.text}"
#     await send_message_with_keyboard(msg, text, reply_kb.menu_btn)
