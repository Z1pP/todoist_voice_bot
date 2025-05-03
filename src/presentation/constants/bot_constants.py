import enum
from typing import Any


class Urls:
    """Константы URL-адресов"""

    TODOIST_DEVELOPER_PORTAL = "https://developer.todoist.com/appconsole.html"


class Emoji:
    """Подборка используемых эмодзи"""

    BACK = "🔙"
    MENU = "🏃"
    TEXT_INPUT = "📝"
    VOICE_INPUT = "🎙️"
    TASK = "📌"
    LIST = "📋"
    STATS = "📊"
    SETTINGS = "⚙️"
    HELP = "❓"
    YES = "✅"
    NO = "❌"
    WARNING = "⚠️"
    LINK = "🔗"


class CommonButtons(str, enum.Enum):
    """Общие кнопки интерфейса"""

    BACK = f"{Emoji.BACK} Назад"
    MENU = f"{Emoji.MENU} В меню"
    CANCEL = "❌ Отмена"


class InputMethod(str, enum.Enum):
    """Методы ввода данных"""

    TEXT = f"{Emoji.TEXT_INPUT} Текстом"
    VOICE = f"{Emoji.VOICE_INPUT} Голосовое"


class MenuButtons(str, enum.Enum):
    """Кнопки главного меню"""

    ADD_TASK = f"{Emoji.TASK} Создать задачу"
    LIST_TASKS = f"{Emoji.LIST} Список задач"
    STATISTICS = f"{Emoji.STATS} Статистика"
    SETTINGS = f"{Emoji.SETTINGS} Настройки"
    HELP = f"{Emoji.HELP} Помощь"


class SettingsButtons(str, enum.Enum):
    """Кнопки настроек"""

    CHANGE_APIKEY = "Изменить API ключи"
    CHANGE_PROJECT = "Изменить проект"
    BACK = CommonButtons.BACK.value


class Answers(str, enum.Enum):
    """Варианты ответов"""

    YES = f"{Emoji.YES} Да"
    NO = f"{Emoji.NO} Нет"


class ExceptionMessages(str, enum.Enum):
    """Сообщения об ошибках"""

    DOWNLOAD_VOICE = "Ошибка при загрузке голосового сообщения"
    TRANSCRIBE_VOICE = "Ошибка при транскрибировании голосового сообщения"
    CREATE_TASK = "Ошибка при создании задачи"
    UNKNOWN = f"{Emoji.WARNING} Произошла ошибка, попробуйте еще раз"


class Messages:
    """Текстовые сообщения бота"""

    class Instruction:
        """Инструкции для пользователя"""

        API_KEY = f"""
        {Emoji.LINK} <b>Как получить API-ключ Todoist:</b>
        
        1. Откройте <a href="{Urls.TODOIST_DEVELOPER_PORTAL}">раздел разработчика</a>
        2. Авторизуйтесь под своим аккаунтом
        3. Скопируйте <b>API Token</b> из <i>Access token</i>
        """

        TASK_INPUT = f"""
        {Emoji.TEXT_INPUT} <b>Как добавить задание?</b>
        
        Вы можете отправить:
        1. Текстовое сообщение
        2. Голосовое сообщение
        """

    class Dialog:
        """Диалоговые сообщения"""

        HELP = "Здесь будет справочная информация"
        MENU = "Привет! Я помогу организовать твои задачи 😊"
        TASK_CREATED = "Задача создана: {task}"
        CONFIRM_TASK = "Я правильно понял?\n\n{task}"
        IN_DEVELOPMENT = "Этот раздел еще в разработке 🛠️"
        ECHO = "Я не понимаю эту команду. Напишите /help"

    class State:
        """Сообщения состояний"""

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
        PROCESSING = "Обрабатываю запрос..."

    @staticmethod
    def format_message(message: str, **kwargs: Any) -> str:
        """Форматирует сообщение с параметрами"""
        return message.format(**kwargs)
