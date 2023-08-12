from ctypes import resize
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_load = KeyboardButton('/Download')
button_delete = KeyboardButton('/cancel')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)