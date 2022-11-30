from flask import render_template, request, redirect

from . import create_app
from .models import *
from .database import *

from flask_security import Security, current_user, auth_required, roles_required, hash_password, SQLAlchemySessionUserDatastore

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

@app.route("/bike<id>", methods=['GET', 'POST'])
@app.route("/bike<id>/<operation>", methods=['GET', 'POST'])
@auth_required()
def bike(id, operation=None):
    ride_db = Ride.query.filter_by(bike_id=id, end_time=None).first()
    if request.method == 'POST':
        if request.content_type == 'application/json':
            ride_req = request.get_json()
        elif request.content_type == 'application/x-www-form-urlencoded':
            ride_req = request.form
        else:
            return "Unknown content type"
        # time format: 2004-10-19 10:23:54
        if operation == 'rent':
            add_instance(Ride, user_id=current_user.id, bike_id=id, start_time=ride_req['start_time'])
            return redirect('/bike' + id)
        elif operation == 'return':                
            edit_instance(Ride, ride_db.id, end_time=ride_req['end_time'])
            return redirect('/bike' + id)

    if ride_db is None:
        status = "rent"
    elif ride_db.user_id == current_user.id:
        status = "return"
    else:
        status = "unavailable"
    bike = get_instance(Bike, id)
    return render_template('bike.html', bike=bike, status=status)

@app.route("/bike-management", methods=['GET', 'POST'])
@app.route("/bike-management/<operation>", methods=['GET', 'POST'])
@auth_required()
@roles_required('bike-manager')
def bike_management(operation = None):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            bike = request.get_json()
        elif request.content_type == 'application/x-www-form-urlencoded':
            bike = request.form
        else:
            return "Unknown request content type"
        if operation == 'add':
            add_instance(Bike, **bike)
            return "Bike added"
        elif operation == 'delete':
            delete_instance(Bike, bike['id'])
            return "Bike deleted"
        elif operation == 'edit':
            edit_instance(Bike, **bike)
            return "Bike edited"
        else:
            return "Unknown operation"
    return render_template('bike_management.html')

# TODO: test this & create user_management.html
@app.route("/user-management", methods=['GET', 'POST'])
@app.route("/user-management/<operation>", methods=['GET', 'POST'])
@auth_required()
@roles_required('user-manager')
def user_management(operation = None):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            roles_users = request.get_json()
        elif request.content_type == 'application/x-www-form-urlencoded':
            roles_users = request.form
        else:
            return "Unknown request content type"
        if operation == 'delete':
            delete_instance(User, roles_users['user_id'])
            # delete related roles
            RolesUsers.query.filter_by(user_id=roles_users['user_id']).delete().all()
            db.session.commit()
            return "User deleted"
        elif operation == 'add-role':
            add_instance(RolesUsers, roles_users['user_id'], roles_users['role_id'])
            return "Role added"
        elif operation == 'remove-role':
            delete_instance(RolesUsers, roles_users['id'])
            return "Role removed"
        else:
            return "Unknown operation"
    return render_template('user_management.html')