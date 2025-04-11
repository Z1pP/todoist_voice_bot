from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.constants import ANSWERS, INPUT_METHODS, MESSAGES
from bot.keyboards.reply import kb
from bot.states import TaskCreationStates
from bot.utils import handle_task_creation, send_message_with_keyboard

router = Router(name="start_commands")


@router.message(Command("start"))
async def start_command(message: Message):
    """
    Обработчик команды /start
    """
    await send_message_with_keyboard(message, MESSAGES["start"])


@router.message(Command("help"))
async def help_command(message: Message):
    """
    Обработчик команды /help
    """
    await send_message_with_keyboard(message, MESSAGES["help"])


@router.message(Command("add_task"))
async def add_task_command(message: Message, state: FSMContext):
    """
    Обработчик начала создания задачи
    """
    await send_message_with_keyboard(message, MESSAGES["choose_input"], kb.type_input)
    # Устанавливаем состояние ожидания выбора метода ввода
    await state.set_state(TaskCreationStates.WAITING_INPUT_METHOD)


@router.message(
    TaskCreationStates.WAITING_INPUT_METHOD, F.text.in_(INPUT_METHODS["text"])
)
async def proccess_text_input(message: Message, state: FSMContext):
    await state.update_data(input_method=message.text)

    await send_message_with_keyboard(message, MESSAGES["waiting_text"])
    # Устанавливаем состояние для подтвеждение введенного
    await state.set_state(TaskCreationStates.WAITING_TEXT_INPUT)


@router.message(TaskCreationStates.WAITING_TEXT_INPUT, F.text)
async def proccess_task_creation(message: Message, state: FSMContext):
    """
    Процесс получения текста
    """
    await handle_task_creation(message, state, message.text)


@router.message(
    TaskCreationStates.WAITING_INPUT_METHOD, F.text.in_(INPUT_METHODS["voice"])
)
async def proccess_voice_input(message: Message, state: FSMContext):
    await state.update_data(input_method=message.text)

    await send_message_with_keyboard(message, MESSAGES["waiting_voice"])
    # Устанавливаем состояние для подтвеждение введенного
    await state.set_state(TaskCreationStates.WAITING_VOICE_INPUT)


@router.message(
    TaskCreationStates.WAITING_CONFIRMATION_TEXT, F.text.in_(ANSWERS["yes"])
)
async def proccess_confirmation_text_yes(message: Message, state: FSMContext):
    data = await state.get_data()
    result_text = data.get("text")

    await message.answer("Создаю задачу...")
    await message.answer(f"Задача создана: {result_text}")
    await state.clear()


@router.message(TaskCreationStates.WAITING_CONFIRMATION_TEXT, F.text.in_(ANSWERS["no"]))
async def proccess_confirmation_text_no(message: Message, state: FSMContext):
    data = await state.get_data()
    input_method = data.get("input_method")

    if input_method == INPUT_METHODS["voice"]:
        await proccess_voice_input(message, state)
        return

    await proccess_text_input(message, state)


@router.message(Command("list_tasks"))
async def list_tasks_command(message: Message):
    await message.answer("Раздел в разработке!")
