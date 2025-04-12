from dataclasses import dataclass

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


@dataclass
class ReplyKeyboards:
    """
    Класс содержит внутри себя все reply кнопки
    """

    @property
    def type_input(self):
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📝 Текстом"), KeyboardButton(text="🎙️ Голосовое")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )

    @property
    def confirm_input(self):
        return ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="✅ Да"), KeyboardButton(text="❌ Нет")]],
            resize_keyboard=True,
            one_time_keyboard=True,
        )

    @property
    def cancel(self):
        return ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="❌ Отмена")]],
            resize_keyboard=True,
            one_time_keyboard=True,
        )


reply_kb = ReplyKeyboards()
