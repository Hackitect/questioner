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

postgres=# CREATE USER questioner with encrypted password 'password123';
CREATE ROLE
postgres=# 

postgres=# GRANT ALL PRIVILEGES ON DATABASE questioner TO questioner;
GRANT
postgres=# \\c questioner = connects to questioner database

questioner=# \\dt
            List of relations
 Schema |   Name    | Type  |   Owner    
--------+-----------+-------+------------
 public | answers   | table | questioner
 public | meetups   | table | questioner
 public | questions | table | questioner
 public | users     | table | questioner
(4 rows)

to drop tables that have relationships use DROP TABLE table_name CASCADE;

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
#Create the tables for the project

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
            createdby INTEGER REFERENCES users(user_id)
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
            cursor.close()
            conn.close()
 
# #snippets
#     cursor = conn.cursor()
#     cursor.execute('SELECT VERSTION()')
#     db_version = cursor.fetchone()
#     print (db_version)

def username_exists(username):
    sql = """SELECT username FROM users;"""
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if username == result:
        # username exists
        return True
     
def email_exists(email):
    sql = """SELECT email FROM users;"""
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if email == result:
        # username exists
        return True

def run_sql(sql):
    conn = None
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def main():
    create_tables()

# The below line is used to call the module directly from command line to test tables creation
# python database.py
if __name__ == ('__main__'):
    main()