import asyncio
import logging

from infrastructure.config.settings import settings
from infrastructure.database.db import initialize_db
from infrastructure.logging.logger import setup_logging
from presentation.bot import initialize_bot

logger = logging.getLogger(__name__)


async def main():
    await initialize_db()

    bot, dp = await initialize_bot(token=settings.BOT_TOKEN)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error("Ошибка при старте бота: ", str(e))


if __name__ == "__main__":
    setup_logging()
    asyncio.run(main())
