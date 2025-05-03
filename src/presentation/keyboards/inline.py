from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from presentation.constants.bot_constants import Messages


class InlineKeyboards:
    @property
    def api_key_url_kb(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=Messages.Instruction.GET_KEY_BUTTON_TEXT,
                        url=Messages.Instruction.DEVELOPER_PORTAL_URL,
                    ),
                ]
            ]
        )


inline_kb = InlineKeyboards()
