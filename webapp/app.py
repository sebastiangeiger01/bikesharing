from flask import render_template, request

from . import create_app
from .models import *
from .database import *

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

# remove this later
@app.route("/add")
def add():
    if not app.security.datastore.find_user(email="test@me.com"):
        app.security.datastore.create_user(email="test@me.com", password=hash_password("password"))
        db.session.commit()
        return "Added user"
    return "User already exists"

# remove this later
@app.route("/hello")
@auth_required()
def hello():
    return render_template('hello.html', email=current_user.email)

# TODO: rent, return functionality
@app.route("/bike-<id>")
@auth_required()
def bike(id):
    bike = get_instance(Bike, id)
    return render_template('bike.html', bike=bike)

# TODO: form
@app.route("/bike-management", methods=['GET', 'POST'])
@app.route("/bike-management/<operation>", methods=['GET', 'POST'])
@auth_required()
def bike_management(operation = None):
    if request.method == 'POST':
        json = request.get_json()
        if operation == 'add':
            add_instance(Bike, **json)
            return "Bike added"
        elif operation == 'delete':
            delete_instance(Bike, json['id'])
            return "Bike deleted"
        elif operation == 'edit':
            edit_instance(Bike, **json)
            return "Bike edited"
    return render_template('bike_management.html')

# TODO: check copilot code delete user? & assign roles
@app.route("/user-management", methods=['GET', 'POST'])
@app.route("/user-management/<operation>", methods=['GET', 'POST'])
@auth_required()
def user_management(operation = None):
    if request.method == 'POST':
        json = request.get_json()
        if operation == 'add':
            add_instance(User, **json)
            return "User added"
        elif operation == 'delete':
            delete_instance(User, json['id'])
            return "User deleted"
        elif operation == 'edit':
            edit_instance(User, **json)
            return "User edited"
    return render_template('user_management.html')