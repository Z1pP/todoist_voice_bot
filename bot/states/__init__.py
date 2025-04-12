from aiogram.fsm.state import State, StatesGroup


class TaskCreationStates(StatesGroup):
    """
    Состояния для создания задачи
    """

    WAITING_CHOICE_INPUT_METHOD = State()
    WAITING_VOICE_INPUT = State()
    WAITING_TEXT_INPUT = State()
    WAITING_CONFIRMATION_TEXT = State()
    WAITING_LLM_PROCESSING = State()
