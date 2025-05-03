# from aiogram import F, Router
# from aiogram.fsm.context import FSMContext
# from aiogram.types import Message

# from bot.constants import MenuButtons, Messages, SettingsButtons
# from bot.keyboards.inline import inline_kb
# from bot.keyboards.reply import reply_kb
# from bot.utils import send_message_with_keyboard

# router = Router(name=__name__)


# @router.message(F.text == MenuButtons.SETTINGS.value)
# async def settings_commands(message: Message):
#     await send_message_with_keyboard(
#         message=message,
#         text="Выберите пункт настроек:",
#         keyboard=reply_kb.settings_menu_btn,
#     )


# @router.message(F.text == SettingsButtons.CHANGE_APIKEY.value)
# async def change_apikey_handler(message: Message, state: FSMContext):
#     await send_message_with_keyboard(
#         message=message,
#         text=Messages.Instruction.API_KEY_INSTRUCTION,
#         keyboard=inline_kb.api_key_url_kb,
#     )
