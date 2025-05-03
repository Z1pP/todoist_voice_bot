# from aiogram import F, Router
# from aiogram.filters import Command
# from aiogram.types import Message

# from bot.commands import Commands
# from bot.constants import CommonButtons, Messages
# from bot.keyboards.reply import reply_kb
# from bot.repositories import UserRepository
# from bot.utils import send_message_with_keyboard

# router = Router(name=__name__)


# @router.message(Command(Commands.start.name))
# async def start_command(message: Message):
#     """
#     Обработчик команды /start
#     """
#     tg_id = message.from_user.id

#     try:
#         # TODO: Вынести в отдельный сервис (UseCase)
#         repository = UserRepository()
#         user = repository.get_by_tgid(tg_id)
#         if not user:
#             user = repository.add_new_profile(tg_id)
#         await send_message_with_keyboard(
#             message, Messages.Dialog.START, reply_kb.menu_btn
#         )
#     # TODO: Сделать нормальный эксепшен
#     except Exception as e:
#         await send_message_with_keyboard(message, str(e))


# @router.message(Command(Commands.help.name))
# async def help_command(message: Message):
#     """
#     Обработчик команды /help
#     """
#     await send_message_with_keyboard(message, Messages.Dialog.HELP)


# @router.message(F.text, F.text == CommonButtons.MENU.value)
# async def cancel_handler(message: Message):
#     """
#     Обработчик кнопки cancel
#     """
#     await send_message_with_keyboard(
#         message, text=Messages.CANCEL_MSG, keyboard=reply_kb.menu_btn
#     )
