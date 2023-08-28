from model import Admin
import crud
import os


#####################################################################
# LOGIN


# switch button between login, profile and admin
def switch_profile_login(session):

    # create an empty dictionary where the data will be stored
    button = {}
    # if an admin is logged in then change the button to 'admin' and calculate the route
    if session.get('admin_id', None):
        button['label'] = 'admin'
        # admin = Admin.query.get(session['admin_id'])
        # button['route'] = get_admin_route(admin)
    # otherwise leave 'login' as a label and set the route back to the login route
    else:
        button['label'] = 'login'
        button['route'] = '/login'
    return button

# get the dynamic route of an admin profile
def get_admin_route(admin):
    admin_route = '/admin/' + str(admin.alias)
    return admin_route