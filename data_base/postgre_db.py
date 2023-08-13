import psycopg2

connection = None

#connection


try:
    
    connection = psycopg2.connect(
        host = "127.0.0.1",
        user = "postgres",
        password = "y",
        database = "inrtu_kidsDB")
    #cursor
    #cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version()"
        )
        
        print(f"Server version: {cursor.fetchone()}")

except Exception as _ex:
    print("[INFO] ERROR", _ex)

finally:
    if connection:
        #cursor.close()
        connection.close()
        print("[INFO] connection closed")
