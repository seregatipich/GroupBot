from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def start_keyboard():
    button = KeyboardButton('Начать опрос')
    return ReplyKeyboardMarkup(resize_keyboard=True).add(button)