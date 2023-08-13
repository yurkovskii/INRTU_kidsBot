import psycopg2
from create_bot import bot


async def sql_add_child_command(state):
    async with state.proxy() as data:
        connection = psycopg2.connect(
            host = "127.0.0.1",
            user = "postgres",
            password = "y",
            database = "inrtu_kidsDB"
        )
        print("[INFO] CONNECTED")
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO food_type VALUES (%s, %s, %s, %s)", tuple(data.values()))
            connection.commit()
        connection.close()