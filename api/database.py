import sqlite3
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash, check_password_hash
import os
from model.logins import *

# specify the  path to the database file
db_file_path = 'volumes/db/userdata.db'
print(db_file_path)
# connect to the db
login_api = Blueprint("login_api", __name__, url_prefix="/api/login")
api = Api(login_api)

conn = sqlite3.connect(db_file_path, check_same_thread=False)
cursor = conn.cursor()
class UserDeletion(Resource):
    def delete(self, username):
        conn = sqlite3.connect(db_file_path, check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()
        if not existing_user:
            conn.close()
        cursor.execute('DELETE FROM users WHERE username = ?', (username,))
        conn.commit()
        conn.close()
class UserRegistration(Resource):
    def post(self):
        conn = sqlite3.connect(db_file_path, check_same_thread=False)
        cursor = conn.cursor()
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return make_response(jsonify(error='Username and password are required'), 400)

        # Connect to the database


        # Check if the username is already taken
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            return make_response(jsonify(error='Username is already taken'), 409)
        # Encrypts the password, and stores it in the database
        hashed_password = generate_password_hash(password)
        cursor.execute('''INSERT INTO users (username, password) VALUES(?, ?)''', (username, hashed_password))
        conn.commit()
        conn.close()

        return make_response(jsonify(message='Registration successful'), 201)
    class Visualize(Resource):
        def get(self):
            data = visualize_users_data()
            return jsonify({'users_data': data})
class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Connect to the database
        conn = sqlite3.connect(db_file_path, check_same_thread=False)
        cursor = conn.cursor()
        # Gets user  
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()
        # If no user, returns an error
        if not user:
            return make_response(jsonify(error='User not found'), 400)
        # If password isn't correct, returns an error
        if not check_password_hash(user[2], password):
            return make_response(jsonify(error='Invalid password'), 409)
        # If the password is right, let user in
        return make_response(jsonify(message='Login successful'), 200)

# Add resource to blueprint
api.add_resource(UserRegistration.Visualize, '/vis')
api.add_resource(UserRegistration, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserDeletion, '/delete/<string:username>')