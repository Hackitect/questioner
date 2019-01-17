import psycopg2
from app.api.v2.utils import database, validators
from flask import json, jsonify


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
       
        
    def save(self, firstname, lastname, email, username, phonenumber, password):

        '''Before we save the user, verify first if username already exists'''
        if database.username_exists(username):
            raise Exception('Username already exist, choose another one')
        if database.email_exists(email):
            raise Exception('Email address already taken, use anohe')

        """ insert a new users into the users table"""
        sql = """INSERT INTO users (firstname, lastname, email,
                username, phonenumber, password)
                VALUES(%s,%s,%s,%s,%s) RETURNING user_id;"""
        
        database.run_sql(sql)

          

        return {
            "message": "User created successfully",
            "username": username,
            "email": email
            # "user_id": user_id
            }
    def login(self, email, password):
        sql = """SELECT password from users where email='" + email +"';"""
        conn = database.db_connect()
        cursor = conn.cursor
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        conn.close
        if password == results:
            return "login successful"
            # return jsonify({"Status": 201, "Message": "User logged in successfully"})
        else:
            return "username or password does not match"

        