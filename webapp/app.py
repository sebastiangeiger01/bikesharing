from flask import render_template

from . import create_app
from .models import *

from flask_security import Security, current_user, auth_required, hash_password, SQLAlchemySessionUserDatastore

app = create_app()

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
app.security = Security(app, user_datastore)

# Views
@app.route("/")
@auth_required()
def home():
    return render_template('hello.html', email=current_user.email)

@app.route("/add")
def add():
    if not app.security.datastore.find_user(email="test@me.com"):
        app.security.datastore.create_user(email="test@me.com", password=hash_password("password"))
        db.session.commit()
        return "Added user"
    return "User already exists"

@app.route("/landing")
def landing():
    return render_template('landing.html')