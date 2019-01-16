import psycopg2
from psycopg2 import Error



try:
    conn = psycopg2.connect(
    user = "questioner",
    password = "password123",
    host = "localhost",
    port = "5432",
    database = "questioner"
    )

    cursor = conn.cursor()
    cursor.execute('SELECT VERSTION()')
    db_version = cursor.fetchone()
    print (db_version)
except (Exception, psycopg2.DatabaseError) as error:
    raise error
finally:
    if (conn):
        cursor.close()
        conn.close()

#Create the users model

def create_user_table():
    pass