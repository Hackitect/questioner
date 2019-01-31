import psycopg2
from psycopg2 import Error
from .sql_queries import tables
# from psycopg2.extras import RealDictCursor
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
class Database:
    
    def db(self):
        try:
            conn = psycopg2.connect(
                host = "localhost",
                dbname = "questioner",
                user = "questioner",
                password = "password123"                
                )
            
            # cursor = conn.cursor
            print ("Successfully connected to database")
            return conn
        except (Exception, psycopg2.DatabaseError) as error:
            raise error
#Create the tables for the project

    def create_tables(self):
        conn = self.db()
        cursor = conn.cursor()
        
        ''' create the tables to be used in the project
            i.e. users, meetups, questions and answers
        '''
        try:               
            for table in tables:
                cursor.execute(table)             
            print("all tables created successfully")
            conn.commit()
            cursor.close()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                # self.cursor.close()
                conn.close()