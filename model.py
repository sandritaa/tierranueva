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
    alias = db.Column(db.String)



 # class representation
    def __repr__(self):
        return f'<Admin admin_id={self.admin_id} fname={self.fname} lname={self.lname} email={self.email} phone={self.phone} city={self.city}> country={self.country} alias={self.alias}>'


# class Volunteer(db.Model):
#     # create volunteers table
#     __tablename__ = 'volunteers'
#     # create attributes
#     volunteer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     fname = db.Column(db.String)
#     lname = db.Column(db.String)
#     email = db.Column(db.String)
#     phone = db.Column(db.String)
#     city = db.Column(db.String)
#     country = db.Column(db.String)
#     password = db.Column(db.String(12))

#  # class representation

#     def __repr__(self):
#         return f'<Volunteer volunteer_id={self.volunteer_id} fname={self.fname} lname={self.lname} email={self.email} phone={self.phone} city={self.city}> country={self.country} alias={self.alias}>'


# class Event(db.Model):
#     # create events table
#     __tablename__ = 'events'
#     # create attributes
#     event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     title = db.Column(db.String)
#     date = db.Column(db.DateTime)
#     description = db.Column(db.String)

#  # add foreign keys
#     volunteer_id = db.Column(
#         db.Integer, db.ForeignKey('volunteers.volunteer_id'))

#     # add relationship
#     volunteer = db.relationship('Volunteer', back_populates='event')

 # class representation

    # def __repr__(self):
    #     return f'<Event event_id={self.event_id} title={self.title} date={self.date} description={self.description} >'


# class Post(db.Model):
#     # create posts table
#     __tablename__ = 'posts'
#     # create attributes
#     post_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     title = db.Column(db.String)
#     date = db.Column(db.DateTime)
#     description = db.Column(db.String)
#     picture_path = db.Column(db.String)

#     # add foreign keys
#     admin_id = db.Column(db.Integer, db.ForeignKey('admins.admin_id'))

#     # add relationship
#     admin = db.relationship('Admin', back_populates='post')
# # class representation

#     def __repr__(self):
#         return f'<Post post_id={self.post_id} title={self.title} date={self.date} description={self.description}>'


def connect_to_db(flask_app, db_uri="postgresql:///tierranuevadb", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
