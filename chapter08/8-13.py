#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, session
from datetime import datetime
from flask import request, render_template

app = Flask(__name__)



from werkzeug.contrib.cache import SimpleCache

CACHE_TIMEOUT = 300

cache = SimpleCache()
cache.timeout= CACHE_TIMEOUT

@app.before_request
def return_cached():
    if not request.values:
        response = cache.get(request.path)
        if response:
            print "got the page from cache"
            return response
    print "Will load the page"
        

@app.after_request
def cache_response(response):
    if not request.values:
        cache.set(request.path, response, CACHE_TIMEOUT)
    return response

@app.route("/get_index")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
