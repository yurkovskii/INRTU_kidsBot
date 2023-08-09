from ctypes import resize
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_menu = KeyboardButton('/menu')
button_schedule = KeyboardButton('/schedule')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(button_menu).insert(button_schedule)