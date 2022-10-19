from flask_security import UserMixin, RoleMixin
from flask_sqlalchemy import *
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
db = SQLAlchemy()

# Flask-Security
class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))
    permissions = Column(UnicodeText)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    fs_uniquifier = Column(String(255), unique=True, nullable=False)
    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary='roles_users', backref=backref('users', lazy='dynamic'))

# Other tables
class Bikes(db.Model):
    __tablename__ = 'bikes'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    x_coordinate = Column(Float)
    y_coordinate = Column(Float)
    image = Column(LargeBinary)

class Rides(db.Model):
    __tablename__ = 'rides'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    bike_id = Column(Integer, ForeignKey('bikes.id'))
    start_time = Column(DateTime())
    end_time = Column(DateTime())