import sqlite3
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash, check_password_hash
import os
from api.database import *

# specify the  path to the database file
db_file_path = 'volumes/db/userdata.db'
print(db_file_path)

# Connect to the database
conn = sqlite3.connect(db_file_path, check_same_thread=False)

cursor = conn.cursor()

#Create the identification table with names and password
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    id INTEGER PRIMARY KEY AUTOINCREMENT
)""")

#Create the table with the user data
username = []
pwd = []
id = []

#combine username, pwd, and id triplets
unique_id = zip(username, pwd, id)

print(unique_id)
# Populate the table
cursor.executemany("INSERT INTO users VALUES (?,?,?)", unique_id)

print("Table created successfully")


