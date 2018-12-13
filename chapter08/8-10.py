#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, session
from datetime import datetime

app = Flask(__name__)

app.secret_key = 'SET_ME_BEFORE_USE_SESSION'

@app.route('/write_session')
def writeSession():
    session['key_time']= datetime.now().strftime('%Y-%m-%d %H:%M:%S')		#将当前时间保存在Session中	
    return session['key_time']  			#返回当前时间
 
@app.route('/read_session')
def readSession():
    return session.get('key_time')			#获得上次调用writeSession时写入的时间，并返回

if __name__ == '__main__':
    app.run()
