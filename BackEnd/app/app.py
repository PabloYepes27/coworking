from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from sqlalchemy import create_engine
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PWD = os.getenv("MYSQL_PWD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DB = os.getenv("MYSQL_DB")

print (MYSQL_DB == 'coworking_dev')
if MYSQL_DB == 'coworking_dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
        MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB)
else:
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, MYSQL_DB)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from controllers.controller import *


if __name__ == "__main__":
    app.run(debug=True)

