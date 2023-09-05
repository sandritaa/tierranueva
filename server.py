
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
from jinja2 import StrictUndefined
from datetime import datetime
import crud
import helper

# create the flask app
app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined

# create home route for GET request
@app.route('/')
def homepage():

    # get login or logout depending if an admin is logged in or not
    login_button = helper.switch_profile_login(session)

    # query all admin to display on homepage
    admin = crud.get_all_admins()

    # render an html and pass admins and login_button as data
    return render_template("home.html",  admins=admin, login_button=login_button)

# create home route for POST request
@app.route('/', methods=['POST'])
def profile_logout_and_delete():

    # get data from form - logout or delete account button
    logout = request.form.get('logout') == 'logout'
    delete = request.form.get('delete_account') == 'delete account'

    # if the logout was clicked then set the session keys to None
    if logout:

        session['admin_id'] = None

    # if delete was clicked then delete the account from the db
    elif delete:
        # to delete admin profile, first the dependencies on that admin in the db have to be deleted
        crud.delete_admin_profile(session['admin_id'])
        db.session.commit()
        session['admin_id'] = None

    # finally go back to the home route for GET request
    return redirect('/')

# create login route
@app.route('/login')
def login():

    # get login or logout depending if an admin is logged in or not
    login_button = helper.switch_profile_login(session)

    # get request from admin to retrieve user input in the server
    user_email = request.args.get('email')
    user_password = request.args.get('password')

    # query from the database if the email and password exist under the same account
    admin = crud.get_admins_by_login(user_email, user_password)

    # if no user or email were entered then re-render the login page
    # could also add this as a requirement in the form (e.g. min length on inputs)
    if not user_email or not user_password:
        return render_template('login.html', login_button=login_button)



    # check if admin query above checks out - if it does, redirect to be below admin route
    if admin:

        # add the logged in admin to the session
        session['admin_id'] = admin.admin_id
        session.modified = True

        # get the admin route since it is a dynamic route depending on the logged in admin
    admin_route = helper.get_admin_route(admin)


    #     # go to the admin route
    # return redirect(admin_route)

    # # if no admin was found then do not login and re route to the login route
    # else:
    
    return redirect('/login')

# create the dynamic admin profile route - the dynamic part is given by the <alias> which is made of the admin alias
@app.route('/admin/<alias>')
def admin_profile(alias):
    # get login or logout depending if an admin is logged in or not
    login_button = helper.switch_profile_login(session)

    # get the admin from the alias
    admin = crud.get_admin_by_alias(alias)

    # if the admin is logged in then go then render the admin profile page
    if session['admin_id'] == admin.admin_id:

        # render the page and pass the logged in admin as data
        return render_template("adminProfile.html", admin=admin, login_button=login_button)

    # if no admin is logged in the redirect to the login page
    else:
        return redirect('/login')
    

# create home route for GET request
@app.route('/about')
def about():

    # # get login or logout depending if an admin is logged in or not
    login_button = helper.switch_profile_login(session)

    # query all admin to display on homepage
    admin = crud.get_all_admins()

    # render an html and pass admins and login_button as data
    return render_template("about.html", admin=admin, login_button=login_button)


# # create register volunterr route
# @app.route('/profile')
# def new_volunteer_profile_form():

#     # simply render the create account page
#     return render_template('createAccount.html')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5002)
