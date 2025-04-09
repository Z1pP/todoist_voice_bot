from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_type_input = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📝 Текстом"), KeyboardButton(text="🎙️ Голосовое")]],
    resize_keyboard=True,
    one_time_keyboard=True,
)
