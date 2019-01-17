import unittest
import psycopg2
from app.api.v2.utils import database

class DatabaseTests(unittest.TestCase):
    def setUp(self):
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
        self.conn = conn

    def Test_to_create_tables(self):
        cursor = self.conn.cursor
        cursor.execute("SELECT username, password from users limit 1;")
        results = cursor.fetchall()
        self.assertEquals(results, 'how to test this?')


if __name__ == '__main__':
    unittest.main()