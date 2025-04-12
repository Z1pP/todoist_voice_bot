from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.constants import ANSWERS, INPUT_METHODS, MENU, MESSAGES
from bot.keyboards.reply import reply_kb
from bot.parser.task_parser import TaskData, TaskParser
from bot.states import TaskCreationStates
from bot.utils import (
    handle_task_creation,
    request_content_to_llm,
    send_message_with_keyboard,
)

router = Router(name=__name__)


@router.message(F.text.in_(MENU["add_task"]))
async def add_task_command(message: Message, state: FSMContext):
    """
    Обработчик начала создания задачи
    """
    await send_message_with_keyboard(
        message, MESSAGES["choose_input"], reply_kb.type_input
    )
    # Устанавливаем состояние ожидания выбора метода ввода
    await state.set_state(TaskCreationStates.WAITING_CHOICE_INPUT_METHOD)


@router.message(
    TaskCreationStates.WAITING_CHOICE_INPUT_METHOD, F.text.in_(INPUT_METHODS["text"])
)
async def proccess_text_input(message: Message, state: FSMContext):
    await state.update_data(input_method=message.text)

    await send_message_with_keyboard(message, MESSAGES["waiting_text"])
    # Устанавливаем состояние для передачи текста в LLM
    await state.set_state(TaskCreationStates.WAITING_LLM_PROCESSING)


@router.message(
    TaskCreationStates.WAITING_CHOICE_INPUT_METHOD, F.text.in_(INPUT_METHODS["voice"])
)
async def proccess_voice_input(message: Message, state: FSMContext):
    await state.update_data(input_method=message.text)

    await send_message_with_keyboard(message, MESSAGES["waiting_voice"])
    # Устанавливаем состояние для подтвеждение введенного
    await state.set_state(TaskCreationStates.WAITING_VOICE_INPUT)


@router.message(TaskCreationStates.WAITING_LLM_PROCESSING)
async def proccess_llm_processing(message: Message, state: FSMContext):
    """
    Процесс проверки и исправления текста LLM
    """
    try:
        result_text = await request_content_to_llm(message.text)
        await handle_task_creation(message, state, result_text)
    except Exception:
        await send_message_with_keyboard(
            message, "Произошла ошибка при работе нашей LLM."
        )


@router.message(
    TaskCreationStates.WAITING_CONFIRMATION_TEXT, F.text.in_(ANSWERS["yes"])
)
async def proccess_confirmation_text_yes(message: Message, state: FSMContext):
    data = await state.get_data()
    result_text = data.get("text")

    # В этом моменте
    # идет логика отправки данных в сервис todoist
    try:
        task_parser = TaskParser()
        task_data: TaskData = await task_parser.parse_llm_response(
            json_string=result_text
        )
        await message.answer("Создаю задачу...")
        await message.answer(f"Задача создана: {task_data.title}")
    except Exception as e:
        await message.answer(str(e))
    finally:
        await state.clear()


@router.message(TaskCreationStates.WAITING_CONFIRMATION_TEXT, F.text.in_(ANSWERS["no"]))
async def proccess_confirmation_text_no(message: Message, state: FSMContext):
    data = await state.get_data()
    input_method = data.get("input_method")

    if input_method == INPUT_METHODS["voice"]:
        await proccess_voice_input(message, state)
        return

    await proccess_text_input(message, state)


@router.message(F.text.in_(MENU["list_tasks"]))
async def list_tasks_command(message: Message):
    await send_message_with_keyboard(
        message, MESSAGES["in_development"], reply_kb.cancel
    )
