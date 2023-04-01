# import sqlalchemy class from the flak-sqlalchemy module
from flask_sqlalchemy import SQLAlchemy

# create an object from the class sqlalchemy
db = SQLAlchemy()


class Admin(db.Model):
    # create admin table
    __tablename__ = 'admins'

    # create attributes
    admin_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    city = db.Column(db.String)
    country = db.Column(db.String)
    password = db.Column(db.String(12))


class Volunteer(db.Model):
    # create volunteers table
    __tablename__ = 'volunteers'
    # create attributes
    volunteer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    city = db.Column(db.String)
    country = db.Column(db.String)
    password = db.Column(db.String(12))


class Event(db.Model):
    # create events table
    __tablename__ = 'events'
    # create attributes
    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    date = db.Column(db.DateTime)
    description = db.Column(db.String)
    picture_path = db.Column(db.String)
    password = db.Column(db.String(12))

    # add foreign keys
    admin_id = db.Column(db.Integer, db.ForeignKey('admins.admin_id'))

    # add relationship
    admin = db.relationship('Admin', back_populates='event')


class Post(db.Model):
    # create posts table
    __tablename__ = 'posts'
    # create attributes
    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    date = db.Column(db.DateTime)
    description = db.Column(db.String)

 # add foreign keys
    volunteer_id = db.Column(
        db.Integer, db.ForeignKey('volunteers.volunteer_id'))

    # add relationship
    volunteer = db.relationship('Volunteer', back_populates='post')
