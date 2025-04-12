import asyncio
import logging
import sys

from bot.create_bot import create_bot
from utils.logger import setup_logging

logger = logging.getLogger(__name__)


async def main():
    try:
        await create_bot()
    except Exception as e:
        logger.error(f"Бот крашнулся по причине: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    setup_logging()
    asyncio.run(main())
