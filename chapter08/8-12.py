#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, session
from datetime import datetime

app = Flask(__name__)



from flask import request, url_for, redirect

@app.route('/index')
def index():
    return "I'm the index page"


@app.route('/redirect_url')
def redirect_url():
    next = request.args.get('next') or url_for('index')	
    return redirect(next)

@app.route('/echo_url')
def echo_url():
    return request.base_url


if __name__ == '__main__':
    app.run()
