import psycopg2
from app.api.v2.utils import database

"""
questioner=# INSERT INTO users (firstname, lastname, email, username, phonenumber, password)
VALUES ('Charles', 'Njenga', 'mwangicharles@gmail.com', 'Hackitect', '0722867603','password123') RETURNING user_id;
 user_id 
---------
       1
(1 row)

INSERT 0 1
questioner=# 

"""

class Users():
    def validate_username(self, username):
        sql = """SELECT username FROM users;"""
        conn = database.db_connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if username == result:
            # username exists
            return True
     def validate_email(self, email):
        sql = """SELECT username FROM users;"""
        conn = database.db_connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if email == result:
            # username exists
            return True
       
        
    def save(self, firstname, lastname, email, username, phonenumber, password):

        '''Before we save the user, verify first if username already exists'''
        if validate_username:
            raise Exception('Username already exist, choose another one')

        """ insert a new users into the users table"""
        sql = """INSERT INTO users (firstname, lastname, email,
                username, phonenumber, password)
                VALUES(%s,%s,%s,%s,%s) RETURNING user_id;"""
        conn_db(sql)        

        return {
            "message": "User created successfully",
            "username": username,
            "email": email
            # "user_id": user_id
            }

def conn_db(sql):
    conn = None
    conn = database.db_connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close
        