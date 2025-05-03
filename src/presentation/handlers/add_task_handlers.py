from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from presentation.constants.bot_constants import MenuButtons
from presentation.states import AddTaskState

router = Router(name=__name__)


@router.message(F.text.in_(MenuButtons.ADD_TASK.value))
async def add_task_handler(msg: Message, state: FSMContext):
    await state.set_state(AddTaskState.WAINTING_INPUT)

    await msg.answer("Жду голосовое сообщение или текстовую запись")


@router.message(AddTaskState.WAINTING_INPUT, F.voice)
async def voice_handler(msg: Message, state: FSMContext):
    await state.set_state(AddTaskState.WAITING_CONFIRMATION_TEXT)

    await msg.reply("Это был Голос!")


@router.message(AddTaskState.WAINTING_INPUT, F.text)
async def text_handler(msg: Message, state: FSMContext):
    await state.set_state(AddTaskState.WAITING_CONFIRMATION_TEXT)

    await msg.reply("Это был Текст!")
