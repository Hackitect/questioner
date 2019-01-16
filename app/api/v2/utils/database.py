import psycopg2
from psycopg2 import Error

"""
hackitect@hackitect-LV:~$ sudo -u postgres psql postgres
[sudo] password for hackitect: 
psql (10.6 (Ubuntu 10.6-0ubuntu0.18.10.1))
Type "help" for help.

postgres=# CREATE DATABASE questioner;
CREATE DATABASE
postgres=# 

"""
def db_connect():
    try:
        conn = psycopg2.connect(
        user = "questioner",
        password = "password123",
        host = "localhost",
        port = "5432",
        database = "questioner"
        )

        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        raise error

# function to call to close the connection

def db_close():
    conn = db_connect()
    cursor = conn.cursor()
    if (conn):
        cursor.close()
        conn.close()

# #Create the users model

def create_tables():
    ''' create the tables to be used in the projec
        i.e. users, meetups, questions and answers
    '''
    tables = (
        """
        CREATE TABLE IF NOT EXISTS users(
            user_id serial PRIMARY KEY,
            firstname VARCHAR(20) NOT NULL,
            lastname VARCHAR(20) NOT NULL,
            username VARCHAR(20) NOT NULL,
            phonenumber VARCHAR(15) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL,
            is_admin bool
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS meetups(
            meetups_id serial PRIMARY KEY,
            topic VARCHAR(30) NOT NULL,
            happeningon TIMESTAMP,
            tags VARCHAR(100)
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS questions(
            questions_id serial PRIMARY KEY,
            createdon TIMESTAMP,
            title VARCHAR(30) NOT NULL,
            body VARCHAR(100) NOT NULL,
            meetupid INTEGER REFERENCES meetups(meetups_id),
            createdby INTEGER REFERENCES users (user_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS answers(
            answers_id serial PRIMARY KEY,
            data VARCHAR NOT NULL
        );
        """)
    conn = None
    try:
        conn = db_connect()
        cursor = conn.cursor()
        for table in tables:
            cursor.execute(table)
            cursor.close()
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
 
# #snippets
#     cursor = conn.cursor()
#     cursor.execute('SELECT VERSTION()')
#     db_version = cursor.fetchone()
#     print (db_version)

def main():
    create_tables()


if __name__ == ('__main__'):
    main()
    


