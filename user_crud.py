import sqlite3

def create_user_with_profile(username, email, age=None, gender=None, address=None):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, email, age, gender, address) 
        VALUES (?, ?, ?, ?, ?)
    ''', (username, email, age, gender, address))
    conn.commit()
    conn.close()

def retrieve_users_by_criteria(criteria):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE ' + criteria)
    users = cursor.fetchall()
    conn.close()
    return users

def update_user_profile(user_id, age=None, gender=None, address=None):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users 
        SET age=?, gender=?, address=?
        WHERE id=?
    ''', (age, gender, address, user_id))
    conn.commit()
    conn.close()

def delete_users_by_criteria(criteria):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE ' + criteria)
    conn.commit()
    conn.close()