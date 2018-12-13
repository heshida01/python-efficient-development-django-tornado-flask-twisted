#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
app = Flask(__name__)

@app.route('/login/<username>')
def show_welcome(username):
    return 'Hi %s' % username    					# show welcome

if __name__ == '__main__':
    app.run()
