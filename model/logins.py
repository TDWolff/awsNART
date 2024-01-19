import sqlite3

db_file_path = 'volumes/db/userdata.db'

# Connect to the database 
conn = sqlite3.connect(db_file_path, check_same_thread=False)

cursor = conn.cursor()

# Create a table for user login data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
def visualize_users_data():
    conn = sqlite3.connect(db_file_path, check_same_thread=False)

    cursor = conn.cursor()
    # get all data
    cursor.execute('SELECT * FROM users')
    users_data = cursor.fetchall()
    print(users_data)
    # process data
    result = []
    for user in users_data:
        result.append(f"Username: {user[0]}, Password: {user[1]}")
    conn.close()
    return result