from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_keyboard():
    keyboard = [
        [InlineKeyboardButton("Нажми меня", callback_data="button_pressed")]
    ]
    return InlineKeyboardMarkup(keyboard)
