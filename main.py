import asyncio
import logging
import sys

from bot.create_bot import create_bot


async def main():
    try:
        await create_bot()
    except Exception as e:
        logging.error("Bot crashed", str(e))
        sys.exit(1)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    asyncio.run(main())
