import psycopg2
from app.api.v2.utils import database
from app.api.v2.utils.validators import Validators
from flask import json, jsonify

db = database.Database()
cursor = db.cursor()


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

class Users(Validators):
    def all(self):

        sql = "SELECT * FROM users"
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    # def __init__(self):
    #     pass

            
    def save(self, firstname, lastname, email, username, phonenumber, password):
        '''Before we save the user, verify first if username already exists'''
        if self.username_exists(username, email):
            raise Exception('Username or email already exist, choose another one')
        # if database.email_exists(email):
        #     raise Exception('Email address already taken, use anohe')
        # if self.is_valid_email(email) is False:
        #     raise Exception("Error, Email choosen does not meet requirements")

        """ insert a new users into the users table"""
        sql = """INSERT INTO users (firstname, lastname, email,
                username, phonenumber, password)
                VALUES(%s,%s,%s,%s,%s,%s) RETURNING user_id;"""
       
        user_id = None
        cursor.execute(sql,
            (firstname, 
            lastname, 
            email, 
            username, 
            phonenumber, 
            password)
            )
        db.conn.commit()
        # cursor.close()

        return {
            "message": "User created successfully",
            "username": username,
            "email": email,
            "user_id": user_id
            }

    def login(self, email, password):
        sql = """SELECT email, password from users where email=%s and password=%s;"""
              
        cursor.execute(sql, (email, password))
        results = cursor.fetchone()
               
        if results:
            return {"Status": 201, "Message": "User logged in successfully"}
        else:
            return {"Status": "username or password does not match"}
    
    def username_exists(self, username, email):
        
        sql = """SELECT username, email FROM users WHERE username=%s or email=%s;"""
        cursor.execute(sql, (username, email,))
        result = cursor.fetchall()
        if result:
            # username exists
            return True    