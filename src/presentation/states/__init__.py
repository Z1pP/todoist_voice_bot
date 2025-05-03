from aiogram.fsm.state import State, StatesGroup


class AddTaskState(StatesGroup):
    """
    Состояния для создания задачи
    """

    WAINTING_INPUT = State()
    WAITING_VOICE_INPUT = State()
    WAITING_TEXT_INPUT = State()
    WAITING_CONFIRMATION_TEXT = State()
    WAITING_LLM_PROCESSING = State()
