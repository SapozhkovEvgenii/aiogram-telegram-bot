from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from create_bot import admins


def main_keyboard(user_telegram_id: int) -> ReplyKeyboardMarkup:
    kb_list = [
        [KeyboardButton(text="About us"), KeyboardButton(text="SignUp")],
        [KeyboardButton(text="Continue as guest")]
    ]
    if user_telegram_id in admins:
        kb_list.append([KeyboardButton(text="Admin panel")])
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return keyboard
