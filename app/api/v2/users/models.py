import psycopg2
from app.api.v2.utils.database import Database
from app.api.v2.utils.validators import Validators
from flask import json, jsonify
from app import create_app, bcrypt
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,
                                get_jwt_identity, jwt_refresh_token_required)

db = Database()
conn = db.db()
cursor = conn.cursor()

"""
questioner=# INSERT INTO users (firstname, lastname, email, username, phonenumber, password)
VALUES ('John', 'Doe', 'johndoe@user.com', 'Johndoe', '0700220022','password123') RETURNING user_id;
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
        user_id = None
        """ insert a new users into the users table"""
        sql = """INSERT INTO users (firstname, lastname, email,
                username, phonenumber, password)
                VALUES(%s,%s,%s,%s,%s,%s) RETURNING user_id;"""
               
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        access_token = create_access_token(identity = 'email')
        cursor.execute(sql,
            (firstname, 
            lastname, 
            email, 
            username, 
            phonenumber, 
            hashed_password)
            )
        conn.commit()
        # cursor.close()

        return {
            "message": "User created successfully",
            "username": username,
            "email": email,
            "user_id": user_id,
            "Access_Token": access_token
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
            # username or email exists
            return True    
