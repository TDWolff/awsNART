import sqlite3
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash, check_password_hash
import os
from api.user import visualize_data
# from model.logins import *

# create blueprint

db_path = "volumes/db/userdata.db"
print("db_path: " + db_path)

login_blueprint = Blueprint('loginapi', __name__, url_prefix='/api/login')
api = Api(login_blueprint)

conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

class UserDeletion(Resource):
    def delete(self, uid):
        conn = sqlite3.connect(db_path, check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (uid,))
        existing_user = cursor.fetchone()
        if not existing_user:
            conn.close()
        cursor.execute('DELETE FROM users WHERE username = ?', (uid,))
        conn.commit()
        conn.close()

class usercreate(Resource):
    def post(self):
        conn = sqlite3.connect(db_path, check_same_thread=False)
        cursor = conn.cursor()
        data = request.get_json()
        usr = data.get('username')
        pwd = data.get('password')

        if not usr or not pwd:
            return make_response(jsonify({'error': 'Missing username or password'}), 400)
        
        cursor.execute('SELECT * FROM users WHERE username = ?', (usr,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            return make_response(jsonify({'error': 'Username already exists'}), 410)
        # Encrypting Pwd + store in db
        hashed_pwd = generate_password_hash(pwd)
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (usr, hashed_pwd))
        conn.commit()
        conn.close()

        return make_response(jsonify({'message': 'User created'}), 201)
    class Visualize(Resource):
        def get(self):
            data = visualize_data()
            return make_response(jsonify(data), 200)
class login(Resource):
    def post(self):
        data = request.get_json()
        uid = data.get('username')
        pwd = data.get('password')

        conn = sqlite3.connect(db_path, check_same_thread=False)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE username = ?', (uid,))
        user = cursor.fetchone()
        conn.close()

        if not user:
            return make_response(jsonify({'error': 'User not found'}), 404)
        if not check_password_hash(user[2], pwd):
            return make_response(jsonify({'error': 'Incorrect password'}), 404)
        return make_response(jsonify({'message': 'User authenticated'}), 200)
    

api.add_resource(usercreate.Visualize, '/vis')
api.add_resource(usercreate, '/register')
api.add_resource(login, '/login')
api.add_resource(UserDeletion, '/delete/<string:username>')