from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from presentation.commands.start_commands import set_commands
from presentation.handlers import register_routers


async def initialize_bot(token: str) -> tuple[Bot, Dispatcher]:
    # Bot
    bot = Bot(
        token=token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    # Установка стартовых команд
    await set_commands(bot=bot)

    # Dispather
    dp = Dispatcher()
    await register_routers(dp=dp)
    return bot, dp
