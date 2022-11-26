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
def home():
    geo = '{"type": "FeatureCollection", "features":[{"type":"Feature","geometry":{"type":"Point","coordinates":[49,50]},"properties":{"id":"1","name":"schnelles Bike1"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[11,50]},"properties":{"id":"2","name":"schnelles Bike2"}}]}'
    return render_template('home.html', geo=geo)

@app.route("/add")
def add():
    if not app.security.datastore.find_user(email="test@me.com"):
        app.security.datastore.create_user(email="test@me.com", password=hash_password("password"))
        db.session.commit()
        return "Added user"
    return "User already exists"

@app.route("/hello")
@auth_required()
def hello():
    return render_template('hello.html', email=current_user.email)

@app.route("/bike/<id>")
def bike(id):
    bike = Bikes.query.filter_by(id=id).first()
    return render_template('bike.html', bike=bike)
