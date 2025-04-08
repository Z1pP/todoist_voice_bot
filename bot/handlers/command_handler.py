from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="start_commands")


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Здарова заебал!:)")


@router.message(Command("help"))
async def help_command(message: Message):
    help_text = """
    Available commands:
    /start - Start the bot
    /help - Show this help message
    /add_task - Add a new task
    /list_tasks - Show your tasks
    """
    await message.answer(help_text)
