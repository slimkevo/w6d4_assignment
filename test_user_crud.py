import unittest
import sqlite3
from user_crud import create_user_with_profile

class TestUserCRUD(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER,
                gender TEXT,
                address TEXT
            )
        ''')

    def tearDown(self):
        self.conn.close()

    def test_create_user_with_profile(self):
        create_user_with_profile('TestUser', 'test@example.com', age=30, gender='Male', address='123 Test St')

        self.cursor.execute("SELECT * FROM users")
        print("Users in the database after insertion:", self.cursor.fetchall())

        self.cursor.execute("SELECT * FROM users WHERE username='TestUser'")
        user = self.cursor.fetchone()
        print("User fetched from database:", user)
        self.assertIsNotNone(user)
        self.assertEqual(user[2], 'test@example.com')
        self.assertEqual(user[3], 30)
        self.assertEqual(user[4], 'Male')
        self.assertEqual(user[5], '123 Test St')

if __name__ == '__main__':
    unittest.main()