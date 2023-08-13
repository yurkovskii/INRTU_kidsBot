from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from create_bot import dp, bot
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from data_base import postgre_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data_base import sql_commands

ID = None

class FSMAdmin(StatesGroup):
    food_photo = State()
    food_name = State()
    food_description = State()
    food_type_num = State()


#Получаем ID админа
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'admin panel', reply_markup=admin_kb.button_case_admin)
    await message.delete()

#Запуск машины состояний

async def cm_start(message : types.Message):
    if message.from_user.id == ID: 
        await FSMAdmin.food_photo.set()
        await message.reply('Download the image')
    

#отмена машины состояний

async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')

#Первый ответ записываем в словарь

async def load_photo(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['food_photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('input name')

#2 ответ записываем в словарь

async def load_name(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['food_name'] = message.text
        await FSMAdmin.next()
        await message.reply('input description')

#3 ответ записываем в словарь

async def load_description(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['food_description'] = message.text
        await FSMAdmin.next()
        await message.reply('input food type')

#4 ответ записываем в словарь и используем данные

async def load_price(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['food_type'] = int(message.text)

        await sql_commands.sql_add_child_command(state)

        await state.finish()


#Инлайн клавиатура
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query : types.CallbackQuery):
    await sql_commands.sql_food_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)

@dp.message_handler(commands='Delete')
async def delete_item(message : types.Message):
    if message.from_user.id == ID:
        read = await sql_commands.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


#Регистрируем хендлеры

def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cancel_handler, state="*", commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(cm_start, commands=['Download'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.food_photo)
    dp.register_message_handler(load_name, state=FSMAdmin.food_name)
    dp.register_message_handler(load_description, state=FSMAdmin.food_description)
    dp.register_message_handler(load_price, state=FSMAdmin.food_type_num)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)