import enum

from aiogram import Bot, types


class Commands(str, enum.Enum):
    start = "Запустить бота"
    help = "Список команд"


async def set_commands(bot: Bot):
    await bot.set_my_commands(
        [
            types.BotCommand(command=comm.name, description=comm.value)
            for comm in Commands
        ]
    )
