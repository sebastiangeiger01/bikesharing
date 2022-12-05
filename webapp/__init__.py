import os

from flask import Flask
from .models import db
from flask_wtf.csrf import CSRFProtect
from . import db_config

csrf = CSRFProtect()

def create_app():
    flask_app = Flask(__name__)
    csrf.init_app(flask_app)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    flask_app.config['SECURITY_PASSWORD_SALT'] = os.environ['SECURITY_PASSWORD_SALT']
    # eneable /register
    flask_app.config['SECURITY_REGISTERABLE'] = True
    # eneable /change
    flask_app.config['SECURITY_CHANGEABLE'] = True
    # Disable pre-request CSRF
    flask_app.config['WTF_CSRF_CHECK_DEFAULT'] = False
    # don't require CSRF token for login, logout, register, forgot_password
    flask_app.config['SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS'] = True
    # require CSRF token only for session and basic authenication, not for token auth
    flask_app.config['SECURITY_CSRF_PROTECT_MECHANISMS'] = ['session', 'basic']
    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()
    return flask_app