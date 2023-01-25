from flask import render_template, request, redirect, jsonify

from . import create_app
from .models import *
from .database import *
from sqlalchemy import *
from datetime import datetime
from flask_security import Security, current_user, auth_required, roles_required, hash_password, SQLAlchemySessionUserDatastore

app = create_app()

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
app.security = Security(app, user_datastore)

# Create roles and default admin
@app.before_first_request
def setup_roles():
    if get_all(Role) == []:
        user_datastore.find_or_create_role('user-manager')
        user_datastore.find_or_create_role('bike-manager')
        app.security.datastore.create_user(email='admin@bikesharing.com', password=hash_password('admin'))
        db.session.commit()
        add_instance(RolesUsers, user_id=1, role_id=1)
        add_instance(RolesUsers, user_id=1, role_id=2)
        db.session.commit()

# Home
# GeoJSON Template: '{"type": "FeatureCollection", "features":[{"type":"Feature","geometry":{"type":"Point","coordinates":[20.0,30.0]},"properties":{"id":"1","name":"Pegasus 500"} },{"type":"Feature","geometry":{"type":"Point","coordinates":[15.0,50.0]},"properties":{"id":"2","name":"Tesla E3000"} },]}'
@app.route("/")
def home():
    #Initialize variables
    geo = '{"type": "FeatureCollection", "features":['
    min_x = 8.212967
    max_x = 8.343430
    min_y = 49.977280
    max_y = 50.021858
    list_x = list()
    list_y = list()
    bikes = get_all(Bike)

    #Loop through bike array
    for current_bike in bikes:
        geo = geo + '{"type":"Feature","geometry":{"type":"Point","coordinates":[' + str(current_bike.x_coordinate) + ',' + str(current_bike.y_coordinate) + ']},"properties":{"id":"' + str(current_bike.id) + '","name":"' + current_bike.name + '"} },'
        list_x.append(current_bike.x_coordinate)
        list_y.append(current_bike.y_coordinate) 
    geo = geo + ']}'

    #Variables to calculate zoom for map startview
    if len(list_x) & len(list_y) != 0:
        min_x=min(list_x)
        min_y=min(list_y)
        max_x=max(list_x)
        max_y=max(list_y)

    return render_template('home.jinja', geo=geo, min_y=min_y, min_x=min_x, max_y=max_y, max_x=max_x)

# JSON with all bikes (id, name, x, y)
@app.route("/allbikes")
@auth_required()
def bikes():
    bikes = get_all(Bike)
    return jsonify(bikes)

# JSON with all users (id, email, roles)
@app.route("/allusers")
@auth_required()
@roles_required('user-manager')
def users():
    users = get_all(User)
    return jsonify(users)

# JSON with all rides (id, user_id, bike_id, start_time, end_time)
@app.route("/allrides")
@auth_required()
@roles_required('user-manager', 'bike-manager')
def rides():
    rides = get_all(Ride)
    return jsonify(rides)

# rent and return bikes
@app.route("/bike<id>", methods=['GET', 'POST', 'PUT'])
@auth_required()
def bike(id):
    ride_db = Ride.query.filter_by(bike_id=id, end_time=None).first()
    if request.method == 'GET':
        if ride_db is None:
            status = "rent"
        elif ride_db.user_id == current_user.id:
            status = "return"
        else:
            status = "unavailable"
        bike = get_instance(Bike, id)
        if bike is None:
            return redirect('/')
        return render_template('bike.jinja', bike=bike, status=status)

    # time format: 2004-10-19 10:23:54
    if request.method == 'POST':
        if ride_db is not None:
            return "already rented"
        else:
            add_instance(Ride, user_id=current_user.id, bike_id=id, start_time=datetime.now())
            return "bike rented"
    elif request.method == 'PUT':  
        if ride_db is None:
            return "return not possible"
        else:
            edit_instance(Ride, ride_db.id, end_time=datetime.now())
            return "bike returned"
    else:
        return "Unknown method"

# bike-managers can add, delet and edit bikes
@app.route("/bike-management", methods=['GET', 'POST', 'PUT', 'DELETE'])
@auth_required()
@roles_required('bike-manager')
def bike_management(operation = None):
    if request.method == 'GET':
        bikes = get_all(Bike)
        return render_template('bike_management.jinja', bikes=bikes)

    if 'application/json' in request.content_type:
        bike = request.get_json()
    else:
        return "Unknown request content type"

    if request.method == 'POST':
        add_instance(Bike, **bike)
        return "Bike added"
    elif request.method == 'DELETE':
        Ride.query.filter_by(bike_id=bike['id']).delete()
        db.session.commit()
        delete_instance(Bike, bike['id'])
        return "Bike deleted"
    elif request.method == 'PUT':
        edit_instance(Bike, **bike)
        return "Bike edited"
    else:
        return "Unknown method"

# user-managers can delete users and assign roles
@app.route("/user-management", methods=['GET', 'PUT', 'DELETE'])
@auth_required()
@roles_required('user-manager')
def user_management(operation = None):
    if request.method == 'GET':
        users = get_all(User)
        return render_template('user_management.jinja', users=users)

    if 'application/json' in request.content_type:
        roles_users = request.get_json()
    else:
        return "Unknown request content type"

    if request.method == 'DELETE':
        RolesUsers.query.filter_by(user_id=roles_users['user_id']).delete()
        Ride.query.filter_by(user_id=roles_users['user_id']).delete()
        db.session.commit()
        delete_instance(User, roles_users['user_id'])
        # delete related roles
        return "User deleted"
    elif request.method == 'PUT':
        if roles_users['operation'] == 'add_role':
            add_instance(RolesUsers, user_id=roles_users['user_id'], role_id=roles_users['role_id'])
            return "Role added"
        elif roles_users['operation'] == 'remove_role':
            id = RolesUsers.query.filter_by(user_id=roles_users['user_id'], role_id=roles_users['role_id']).first().id
            delete_instance(RolesUsers, id=id)
            return "Role removed"
        else:
            return "Unknown operation"