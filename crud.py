from model import connect_to_db, db, Admin
from sqlalchemy import func


#####################################################################
# ADMIN

# get all artists
def get_all_admins():
    return Admin.query.all()

# delete admin
def delete_admin_profile(admin_id):
    Admin.query.filter(Admin.admin_id == customer_id).delete()

#  get admin by login
def get_artist_by_login(email, password):
    return Admin.query.filter((Admin.email == email) & (
        Admin.password == password)).first()
# get admin by alias
def get_artist_by_alias(alias):
    return Artist.query.filter(Artist.alias == alias).first()