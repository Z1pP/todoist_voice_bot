from aiogram import Bot, types

commands = [("start", "Запустить бота"), ("help", "Список команд")]


async def set_commands(bot: Bot):
    await bot.set_my_commands(
        [
            types.BotCommand(command=command[0], description=command[1])
            for command in commands
        ]
    )
