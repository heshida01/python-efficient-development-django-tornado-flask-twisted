#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
app = Flask(__name__)

@app.route('/Message', methods=[ 'POST'])
def do_send():
    print "This is for POST methods"

@app.route('/Message', methods=['GET'])
def show_the_send_form():
    print "This is for GET methods"


if __name__ == '__main__':
    app.run()
