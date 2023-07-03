from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def start_keyboard() -> ReplyKeyboardMarkup:
    """
    Constructs and returns a Telegram reply keyboard markup object containing a single button 'Start survey'.

    This keyboard can be used to send a prompt to the user to start the survey.

    Returns:
    ReplyKeyboardMarkup: A markup object that includes a 'Start survey' button.
    """
    
    button = KeyboardButton('Начать опрос')
    return ReplyKeyboardMarkup(resize_keyboard=True).add(button)