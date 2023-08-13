import psycopg2

connection = None


try:
    #connection
    connection = psycopg2.connect(
        host = "127.0.0.1",
        user = "postgres",
        password = "y",
        database = "inrtu_kidsDB"
    )
    connection.autocommit = True
    
    #cursor
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version()"
        )
        
        print(f"Server version: {cursor.fetchone()}")

    #create a new table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS all_kids_list(
                kid_id bigint PRIMARY KEY,
                Family_name varchar(50) NOT NULL,
                Given_name varchar(50) NOT NULL,
                Second_name varchar(50),
                Food_type_one integer,
                Food_type_two integer,
                Food_type_three integer,
                Food_type_four integer,
                Food_type_five integer,
                activity_type_id integer)"""
        )
        connection.commit()
        print("[INFO] TABLE CREATED SUCCESSFULLY")

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS food_type(
                    food_photo varchar,
	                food_name varchar(50) PRIMARY KEY,
	                food_description varchar(100),
                    food_type_num varchar(1))"""
                    )
        connection.commit()
        print("[INFO] TABLE CREATED SUCCESSFULLY")

except Exception as _ex:
    print("[INFO] ERROR", _ex)

finally:
    if connection:
        #cursor.close()
        connection.close()
        print("[INFO] connection closed")
