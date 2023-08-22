
from model import *
from datetime import datetime
import os
import json
import crud


# Drop and create db
os.system('dropdb tierranuevadb')
os.system('createdb tierranuevadb')


# Connect to the db and create tables
if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()

# Open the json with mockdata and parse it
# Second argument "r" -> read permission - can only read file
with open("static/data/mockdata.json", "r") as json_file:
    mockdata = json.load(json_file)

# Seed admins in database
admins = mockdata['admins']
for admin in admins:
    db.session.add(crud.create_admin_profile(fname=admin['fname'], lname=admin['lname'], email=admin['email'], phone = admin['phone'], city = admin['city'], password=admin['password'],
                   country=admin['country']))
db.session.commit()

# Seed volunteers in database
volunteers = mockdata['volunteers']
for volunteer in volunteers:
    db.session.add(crud.create_volunteer_profile(
        fname=volunteer['fname'], lname=volunteer['lname'], email=volunteer['email'], phone=volunteer['phone'], password=volunteer['password'] , city = admin['city'], country=admin['country']))
db.session.commit()

# Seed events in database
events = mockdata['events']
for event in events:
    db.session.add(crud.create_event(title = event['title'], description=event['description'], date=datetime.strptime(event['date'], "%Y-%m-%d"), ))
db.session.commit()

# Seed posts in database
posts = mockdata['posts']
for post in posts:
    db.session.add(crud.create_post(title = post['title'], description=post['description'], date=datetime.strptime(post['date'], "%Y-%m-%d"), ))
db.session.commit()