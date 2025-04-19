import enum
from typing import Any


class CommonButtons(str, enum.Enum):
    BACK = "Назад"
    CANCEL = "Отмена"


class InputMethod(str, enum.Enum):
    TEXT = "📝 Текстом"
    VOICE = "🎙️ Голосовое"


class MenuButtons(CommonButtons):
    ADD_TASK = "📝 Создать задачу"
    LIST_TASKS = "📋 Список задач"
    STATISTICS = "📊 Статистика"
    SETTINGS = "⚙️ Настройки"
    HELP = "Помощь"


class SettingsButtons(CommonButtons):
    CHANGE_APIKEY = "Изменить API ключи"
    CHANGE_PROJECT = "Изменить проект"


class Answers(str, enum.Enum):
    YES = "✅ Да"
    NO = "❌ Нет"


class ExceptionMessages(str, enum.Enum):
    DOWNLOAD_VOICE = "Ошибка при загрузке голосового сообщения"
    TRANSCRIBE_VOICE = "Ошибка при транскрибировании голосового сообщения"
    CREATE_TASK = "Ошибка при создании задачи"
    UNKNOWN = "Произошла ошибка, попробуйте еще раз"


class Messages(str, enum.Enum):
    """Все текстовые сообщения бота."""

    START = "Здарова заебал! :)"
    CHOOSE_INPUT = "Как будешь вводить задание?"
    WAITING_TEXT = "Жду текст задания:"
    WAITING_VOICE = "Жду голосовое:"
    CREATING_TASK = "Создаю задачу..."
    TASK_CREATED = "Задача создана: {task}"
    CONFIRM_TASK = "Я правильно понял?\n\n{task}"
    IN_DEVELOPMENT = "Раздел в разработке!"
    ECHO = "Я тебя не понимаю. Напиши /start"

    def format(self, **kwargs: Any) -> str:
        """Форматирует сообщение с переданными параметрами."""
        return self.value.format(**kwargs)
