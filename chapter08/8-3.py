#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
app = Flask(__name__)

from flask import abort, redirect

@app.route('/')
def index():
    return redirect('/check')					#重定向到/login页面

@app.route('/check')
def f_check():
    abort(401)								#立即向客户端返回401错误
#    dont_coding_here()						#这里的代码不会被执行

if __name__ == '__main__':
    app.run()
