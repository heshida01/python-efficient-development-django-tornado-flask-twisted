#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, session
from datetime import datetime

app = Flask(__name__)

app.secret_key = 'SET_ME_BEFORE_USE_SESSION'


from flask import g

class MyDB():
    def __init__(self):
        print "A db connection is created"
    def close(self):
        print "A db is closed"

def connect_to_database():
    return MyDB()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db=connect_to_database()
	g._database = db
    return db

@app.teardown_request
def teardown_db(response):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def login():
    db=get_db()									#第一次调用get_db
    session["has_login"] = True
    # use db to check username and password in database

@app.route('/view_list')
def view_list():
    if "has_login" not in session:
        login()
    db=get_db()									#第二次调用get_db		
    # use db to query data from database.
    return "teardown_db() will be called automatically"


if __name__ == '__main__':
    app.run()
