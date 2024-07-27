from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Отмена'))
start_buttons = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True,
                                    row_width=2).add(KeyboardButton('/start'), KeyboardButton('/info'))

