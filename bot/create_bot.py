import logging

from aiogram import Bot, Dispatcher

from bot.commands import set_commands
from bot.handlers import include_routers
from config import settings

log = logging.getLogger(__name__)


async def create_bot():
    bot = Bot(token=settings.bot_token)
    # Установка команд
    await set_commands(bot)
    dp = Dispatcher()
    # Регистрируем роутеры в боте
    include_routers(dp)
    try:
        await dp.start_polling(bot)
    except Exception as e:
        log.error("Error starting bot: ", str(e))
