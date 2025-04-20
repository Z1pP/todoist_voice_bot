import enum
from typing import Any


class CommonButtons(str, enum.Enum):
    """
    Общие кнопки, используемые в разных частях бота.

    Attributes:
        BACK: Кнопка возврата назад
        CANCEL: Кнопка отмены действия
    """

    BACK = "🔙 Назад"
    CANCEL = "🛑 Отмена"


class InputMethod(str, enum.Enum):
    """
    Методы ввода информации в боте.

    Attributes:
        TEXT: Ввод текстового сообщения
        VOICE: Ввод голосового сообщения
    """

    TEXT = "📝 Текстом"
    VOICE = "🎙️ Голосовое"


class MenuButtons(str, enum.Enum):
    """
    Кнопки главного меню бота.

    Attributes:
        ADD_TASK: Создание новой задачи
        LIST_TASKS: Просмотр списка задач
        STATISTICS: Просмотр статистики
        SETTINGS: Настройки бота
        HELP: Получение справки
    """

    ADD_TASK = "📝 Создать задачу"
    LIST_TASKS = "📋 Список задач"
    STATISTICS = "📊 Статистика"
    SETTINGS = "⚙️ Настройки"
    HELP = "Помощь"


class SettingsButtons(str, enum.Enum):
    """
    Кнопки меню настроек.

    Attributes:
        CHANGE_APIKEY: Изменение API ключей
        CHANGE_PROJECT: Изменение текущего проекта
        BACK: Возврат в предыдущее меню
        CANCEL: Отмена текущего действия
    """

    CHANGE_APIKEY = "Изменить API ключи"
    CHANGE_PROJECT = "Изменить проект"
    BACK = CommonButtons.BACK.value
    CANCEL = CommonButtons.CANCEL.value


class Answers(str, enum.Enum):
    """
    Кнопки для ответов пользователя.

    Attributes:
        YES: Положительный ответ
        NO: Отрицательный ответ
    """

    YES = "✅ Да"
    NO = "❌ Нет"


class ExceptionMessages(str, enum.Enum):
    """
    Сообщения об ошибках.

    Attributes:
        DOWNLOAD_VOICE: Ошибка при скачивании голосового сообщения
        TRANSCRIBE_VOICE: Ошибка при преобразовании голоса в текст
        CREATE_TASK: Ошибка при создании задачи
        UNKNOWN: Неизвестная ошибка
    """

    DOWNLOAD_VOICE = "Ошибка при загрузке голосового сообщения"
    TRANSCRIBE_VOICE = "Ошибка при транскрибировании голосового сообщения"
    CREATE_TASK = "Ошибка при создании задачи"
    UNKNOWN = "Произошла ошибка, попробуйте еще раз"


class Messages(str, enum.Enum):
    """
    Текстовые сообщения бота.

    Attributes:
        START: Приветственное сообщение
        HELP: Справочное сообщение
        CHOOSE_INPUT: Выбор метода ввода
        WAITING_TEXT: Ожидание текстового ввода
        WAITING_VOICE: Ожидание голосового сообщения
        CREATING_TASK: Процесс создания задачи
        TASK_CREATED: Подтверждение создания задачи
        CONFIRM_TASK: Запрос подтверждения задачи
        IN_DEVELOPMENT: Сообщение о незавершенном функционале
        ECHO: Сообщение при неизвестной команде

    Methods:
        format: Форматирует сообщение с переданными параметрами
    """

    START = "Здарова заебал! :)"
    HELP = "Оставь надежду всяк сюда входящий "
    WAITING_INPUT = (
        "📝 <b>Как добавить задание?</b>\n\n"
        "Вы можете отправить мне:\n"
        "1️⃣ <b>Текстовое сообщение</b> — просто напишите задание. "
        "Если заданий несколько, пронумеруйте их:\n"
        "   <i>1. Позвонить клиенту\n"
        "   2. Отправить отчёт</i>\n\n"
        "2️⃣ <b>Голосовое сообщение</b> — продиктуйте ваши задачи. "
        "Пожалуйста, чётко проговаривайте номера заданий:\n"
        "   <i>«Первое. Позвонить клиенту. Второе. Отправить отчёт»</i>\n\n"
        "💡 <b>Совет:</b> Чем конкретнее задание, тем лучше! Например:\n"
        "   ❌ <s>«Сделать отчёт»</s>\n"
        "   ✅ <b>«Подготовить финансовый отчёт за апрель к 15 мая»</b>\n\n"
        "Я готов принять ваши задания в любом удобном формате! 🚀"
    )
    WAITING_TEXT = "Жду текст задания:"
    WAITING_VOICE = "Жду голосовое:"
    CREATING_TASK = "Создаю задачу..."
    TASK_CREATED = "Задача создана: {task}"
    CONFIRM_TASK = "Я правильно понял?\n\n{task}"
    IN_DEVELOPMENT = "Раздел в разработке!"
    ECHO = "Я тебя не понимаю. Напиши /start"

    def format(self, **kwargs: Any) -> str:
        """
        Форматирует сообщение, подставляя переданные параметры.

        Args:
            **kwargs: Именованные аргументы для форматирования строки

        Returns:
            str: Отформатированное сообщение

        Example:
            >>> Messages.TASK_CREATED.format(task="Купить молоко")
            'Задача создана: Купить молоко'
        """
        return self.value.format(**kwargs)
