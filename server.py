
from flask import Flask, render_template, request, flash, session, redirect, flash
from model import connect_to_db, db
from jinja2 import StrictUndefined
from datetime import datetime
# import crud
# import helper
# import keys


# create the flask app
app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5002)