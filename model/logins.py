from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from flask import sqlalchemy, sqlite3
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

# specify the  path to the database file
db_file_path = 'volumes/db/userdata.db'
print(db_file_path)

class Post(db.Model):
    uid = db.Column(db.Integer, primary_key=True, unique=True)
    userid = db.Column(db.Intenger, db.ForeignKey('user.userid'))

    def __init__(self, userid):
        self.userid = userid


