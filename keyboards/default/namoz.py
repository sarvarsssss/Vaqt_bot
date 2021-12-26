from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Uzbek'),
            KeyboardButton(text='English')
        ],
        [
            KeyboardButton(text='Log Out',)
        ],
    ],
    resize_keyboard=True
)
