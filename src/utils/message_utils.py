from aiogram.types import Message


async def send_message_with_keyboard(msg: Message, text: str, keyboard) -> None:
    await msg.answer(text, reply_markup=keyboard)
