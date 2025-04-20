import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.commands import set_commands
from bot.handlers import include_routers
from config import settings

logger = logging.getLogger(__name__)


async def create_bot():
    # Создание бота
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    # Установка команд
    await set_commands(bot)

    dp = Dispatcher()
    # Регистрируем роутеры в боте
    include_routers(dp)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error("Ошибка при старте бота: ", str(e))
