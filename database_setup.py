import sqlite3

def initialize_database():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER,
            gender TEXT,
            address TEXT
        );
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()