#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
app = Flask(__name__)

@app.route('/school/')
def schools():
    return 'The school page'

@app.route('/student')
def students():
    return 'The student page'

if __name__ == '__main__':
    app.run()
