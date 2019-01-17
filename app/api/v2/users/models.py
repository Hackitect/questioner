import psycopg2
from app.api.v2.utils import database


class Users():
    def save(self, firstname, lastname, email, username, phonenumber, password):
        """ insert a new users into the users table"""
        sql = """INSERT INTO users firstname, lastname, email,
                username, phonenumber, password
                VALUES(%s,%s,%s,%s,%s) RETURNING user_id;"""
        conn = None
        user_id = None

        conn = database.db_connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        user_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close

        return {
            "message": "User created successfully",
            "username": username,
            "email": email,
            "user_id": user_id
            }
        