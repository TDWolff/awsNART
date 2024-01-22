from flask import Flask, request, jsonify, Blueprint
import sqlite3
import hashlib

login_api = Blueprint('login_api', __name__)
app = Flask(__name__)

@login_api.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Hash the password before storing it in the database
    password_hash = hash_password(password)

    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    try:
        # Insert user information into the database
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
        conn.commit()
        return jsonify({'message': 'User registered successfully'})
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists'}), 400
    finally:
        conn.close()

def hash_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

if __name__ == '__main__':
    app.run(debug=True)
