#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
app = Flask(__name__)

@app.route('/add/<int:number>')
def add_one(number):
    return '%d' % (number+1)						# return the result after plus one

if __name__ == '__main__':
    app.run()
