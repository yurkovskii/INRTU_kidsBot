from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot

async def echo_send(message : types.Message):
    if message.text == 'Hello':
        await message.answer('Hi there!')
        
def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)