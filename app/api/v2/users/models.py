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
except (Exception, psycopg2.DatabaseError) as error:
    raise error
finally:
    if conn:
        conn.close()

#Create the users model