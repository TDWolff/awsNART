import sqlite3



db_path = 'volumes/db/userdata.db'
print("db_path: " + db_path)

conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
               username TEXT NOT NULL,
               password TEXT NOT NULL,
    )
''')


def visualize_data():
    conn = sqlite3.connect(db_path, check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    print(data)
    result = []

    for users in data:
        result = []
        for user in data:
            result.append(f"Username: {user[0]}, Password: {user[1]}")
    conn.close()
    return result