from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other
#from data_base import sqlite_db
from data_base import postgre_db

async def on_startup(_):
    print('bot is online now *_*')
    #postgre_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)