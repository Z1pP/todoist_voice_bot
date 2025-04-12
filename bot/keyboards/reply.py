from dataclasses import dataclass

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.constants import ANSWERS, INPUT_METHODS, MENU


@dataclass
class ReplyKeyboards:
    """
    Класс содержит внутри себя все reply кнопки
    """

    @property
    def menu(self):
        buttons = [KeyboardButton(text=value) for key, value in MENU.items()]
        return ReplyKeyboardMarkup(
            keyboard=[
                buttons[:3],
                buttons[3:],
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )

    @property
    def type_input(self):
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=value) for key, value in INPUT_METHODS.items()]
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )

    @property
    def confirm_input(self):
        return ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text=value) for key, value in ANSWERS.items()]],
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
