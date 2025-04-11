from typing import Optional

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup

from bot.constants import MESSAGES
from bot.keyboards.reply import reply_kb
from bot.states import TaskCreationStates
from services.llm import LlmClient


async def send_message_with_keyboard(
    message: Message, text: str, keyboard: Optional[ReplyKeyboardMarkup] = None
):
    await message.answer(text, reply_markup=keyboard)


async def handle_task_creation(message: Message, state: FSMContext, task_text: str):
    await state.update_data(text=task_text)
    await send_message_with_keyboard(
        message, MESSAGES["confirm_task"].format(task=task_text), reply_kb.confirm_input
    )
    await state.set_state(TaskCreationStates.WAITING_CONFIRMATION_TEXT)


async def request_content_to_llm(content: str) -> str:
    client = LlmClient()
    return await client.make_request_async(content)
