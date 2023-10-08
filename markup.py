from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_keyboard():
    kb_main = [
        [KeyboardButton(text="Создать")],
        [KeyboardButton(text="Найти человека")]
    ]
    main_kb = ReplyKeyboardMarkup(keyboard=kb_main, resize_keyboard=True)
    return main_kb


def find_by():
    kb_main = [
        [KeyboardButton(text="ID")],
        [KeyboardButton(text="TG")],
        [KeyboardButton(text="CHANEL")],
        [KeyboardButton(text="НАЗАД")],
    ]
    main_kb = ReplyKeyboardMarkup(keyboard=kb_main, resize_keyboard=True)
    return main_kb
