from dataclasses import dataclass

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.constants import (
    Answers,
    CommonButtons,
    InputMethod,
    MenuButtons,
    SettingsButtons,
)


@dataclass
class ReplyKeyboards:
    """
    Класс содержит внутри себя все reply кнопки
    """

    @property
    def menu_btn(self):
        buttons = [KeyboardButton(text=button.value) for button in MenuButtons]
        return ReplyKeyboardMarkup(
            keyboard=[
                buttons[:3],
                buttons[3:],
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )

    @property
    def type_input_btn(self):
        return ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text=button.value) for button in InputMethod]],
            resize_keyboard=True,
            one_time_keyboard=True,
        )

    @property
    def answer_btn(self):
        return ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text=button.value) for button in Answers]],
            resize_keyboard=True,
            one_time_keyboard=True,
        )

    @property
    def cancel_btn(self):
        return ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text=button.value) for button in CommonButtons]],
            resize_keyboard=True,
            one_time_keyboard=True,
        )

    @property
    def settings_menu_btn(self):
        buttons = [[KeyboardButton(text=button.value) for button in SettingsButtons]]
        return ReplyKeyboardMarkup(
            keyboard=[
                buttons[:2],
                buttons[2:],
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )


reply_kb = ReplyKeyboards()
