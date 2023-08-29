from model import connect_to_db, db, Admin
from sqlalchemy import func


#####################################################################
# ADMIN

# get all admins
def get_all_admins():
    return Admin.query.all()

# delete admin
def delete_admin_profile(admin_id):
    Admin.query.filter(Admin.admin_id == admin_id).delete()

#  get admin by login
def get_admins_by_login(email, password):
    return Admin.query.filter((Admin.email == email) & (
        Admin.password == password)).first()
# get admin by alias
def get_admin_by_alias(alias):
    return Admin.query.filter(Admin.alias == alias).first()


# create admin profile to seed database
def create_admin_profile(fname, lname, email, phone, password, country, city, alias):
    return Admin(fname=fname, lname=lname, email=email, password=password, country=country,
                  alias=alias, city=city, phone=phone)

if __name__ == "__main__":
    from server import app

    connect_to_db(app)