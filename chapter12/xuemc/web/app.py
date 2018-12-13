import sys, os
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+pg8000://postgres:password@localhost/bd'
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'you-will-never-..guess'


