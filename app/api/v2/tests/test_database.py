import unittest
import psycopg2
from psycopg2 import Error
from app.api.v2.utils import database

class DatabaseTests(unittest.TestCase):
    def init__(self):
        self.conn = conn

    def setUp(self):
        global conn
                 
        try:
            conn = psycopg2.connect(
                host = 'localhost',
                database = 'questioner',
                user = 'questioner',
                password = 'password123',
                port = '5432'
            )
            return conn
        except (Exception, psycopg2.DatabasError) as error:
            raise error     

    def tearDown(self):
        conn.close()
    
    def Test_to_create_tables(self):
        self.cursor = conn.cursor
        self.cursor.execute("SELECT username, password from users limit 1;")
        results = self.cursor.fetchall()
        self.cursor.close()
        self.assertIn(results, 'password123')


if __name__ == '__main__':
    unittest.main()