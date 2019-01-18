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
class Database():
    
    def __init__(self):
        
        self.host = 'localhost',
        self.name = 'questioner',
        self.user = 'questioner',        
        self.password = 'password123'
        
        try:
            self.conn = psycopg2.connect(
                host = self.host,
                dbname = self.name,
                user = self.user,
                password = self.password                
                )
            
            self.cursor = self.conn.cursor
        
        except (Exception, psycopg2.DatabaseError) as error:
            raise error
#Create the tables for the project

    def create_tables(self):
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
        self.conn = None
        try:            
            for table in tables:
                self.cursor.execute(table)
            self.cursor.close()
            self.conn.commit()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if self.conn is not None:
                self.cursor.close()
                self.conn.close()
  
    # def username_exists(self, username):
    #     sql = """SELECT username FROM users;"""
    #     conn = db_connect()
    #     cursor = conn.cursor()
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     if username == result:
    #         # username exists
    #         return True
        
    # def email_exists(self, email):
    #     sql = """SELECT email FROM users;"""
    #     conn = db_connect()
    #     cursor = conn.cursor()
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     if email == result:
    #         # username exists
    #         return True  