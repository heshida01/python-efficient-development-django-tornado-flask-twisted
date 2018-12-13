#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
app = Flask(__name__)

from flask import abort, redirect

from flask import render_template

@app.route('/')
def f_check():
    abort(400)								#立即向客户端返回401错误

@app.errorhandler(400)
def bad_request(error):
    return render_template('bad_request.html'), 400

if __name__ == '__main__':
    app.run()
