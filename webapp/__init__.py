import os

from flask import Flask

from .models import db
from . import db_config


def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    flask_app.config['SECURITY_PASSWORD_SALT'] = os.environ['SECURITY_PASSWORD_SALT']
    flask_app.config['SECURITY_REGISTERABLE'] = True
    flask_app.config['SECURITY_CHANGEABLE'] = True
    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()
    return flask_app