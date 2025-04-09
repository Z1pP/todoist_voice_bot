from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.keyboards.reply import kb_type_input

router = Router(name="start_commands")


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Здарова заебал!:)")


@router.message(Command("help"))
async def help_command(message: Message):
    await message.delete()

    help_text = """
    Available commands:
    /start - Start the bot
    /help - Show this help message
    /add_task - Add a new task
    /list_tasks - Show your tasks
    """
    await message.answer(help_text)


@router.message(Command("add_task"))
async def add_task_command(message: Message):
    await message.delete()
    await message.answer(text="Как будешь вводить задание?", reply_markup=kb_type_input)


@router.message(Command("list_tasks"))
async def list_tasks_command(message: Message):
    await message.delete()
    await message.answer("Раздел в разработке!")
