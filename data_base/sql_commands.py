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
        print("[INFO] CONNECTED TO DB")
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO food_type VALUES (%s, %s, %s, %s)", tuple(data.values()))
            connection.commit()
            print("[INFO] INFORMATION WAS ADDED")
        
        connection.close()
        print("[INFO] DISCONNECTED FROM DB")


async def sql_read_food_type(message):
    connection = psycopg2.connect(
        host = "127.0.0.1",
        user = "postgres",
        password = "y",
        database = "inrtu_kidsDB"
    )
    print("[INFO] CONNECTED TO DB")
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM food_type")
        results = cursor.fetchall()

        for result in results:
            await bot.send_photo(message.from_user.id, result[0], f'{result[1]}\nОписание: {result[2]}\nТип комбо: {result[-1]}')
            connection.commit()
    
    connection.close()
    print("[INFO] DISCONNECTED FROM DB")