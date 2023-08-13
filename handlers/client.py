from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import postgre_db
from data_base import sql_commands

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hello, you are going to give yor kid the best afterschool time ever', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('you need to start conversation with bot:\n @inrtu_after_school_bot')

async def command_food(message : types.Message):
        # await bot.send_message(message.from_user.id, 'food')
        await sql_commands.sql_read_food_type(message)

async def command_schedule(message : types.Message):
        await bot.send_message(message.from_user.id, 'schedule')


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_food, commands=['menu'])
    dp.register_message_handler(command_schedule, commands=['schedule'])