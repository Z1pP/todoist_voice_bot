import logging
from typing import Optional

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup

from bot.constants import Messages
from bot.keyboards.reply import reply_kb
from bot.states import TaskCreationStates
from services.llm import LlmClientAsync

logger = logging.getLogger(__name__)


async def send_message_with_keyboard(
    message: Message, text: str, keyboard: Optional[ReplyKeyboardMarkup] = None
):
    """
    Отправляет сообщение пользователю с опциональной клавиатурой.

    Args:
        message (Message): Объект сообщения Telegram
        text (str): Текст сообщения для отправки
        keyboard (Optional[ReplyKeyboardMarkup]): Клавиатура для отображения.
            По умолчанию None.

    Returns:
        None

    Example:
        await send_message_with_keyboard(
            message,
            "Выберите действие:",
            reply_kb.main_menu
        )
    """
    await message.answer(text, reply_markup=keyboard)


async def handle_task_creation(message: Message, state: FSMContext, task_text: str):
    """
    Обрабатывает процесс создания новой задачи.

    Функция сохраняет текст задачи в состоянии, отправляет сообщение
    для подтверждения создания задачи и устанавливает состояние ожидания
    подтверждения.

    Args:
        message (Message): Объект сообщения Telegram
        state (FSMContext): Контекст состояния FSM
        task_text (str): Текст создаваемой задачи

    Returns:
        None

    Example:
        await handle_task_creation(
            message,
            state,
            "Купить молоко завтра"
        )
    """
    await state.update_data(text=task_text)
    await send_message_with_keyboard(
        message,
        Messages.CONFIRM_TASK.value.format(task=task_text),
        reply_kb.answer_btn,
    )
    await state.set_state(TaskCreationStates.WAITING_CONFIRMATION_TEXT)


async def request_content_to_llm(content: str) -> str:
    """
    Отправляет контент на обработку языковой модели (LLM).

    Создает асинхронный клиент LLM и отправляет содержимое на обработку.

    Args:
        content (str): Текстовое содержимое для обработки LLM

    Returns:
        str: Ответ от языковой модели

    Raises:
        Exception: Может вызвать исключение при проблемах с подключением
            или обработкой запроса

    Example:
        response = await request_content_to_llm(
            "Преобразуй этот текст в задачу"
        )
    """
    client = LlmClientAsync()
    return await client.make_request_async(content)
