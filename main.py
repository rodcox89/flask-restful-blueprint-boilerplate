#!/usr/bin/env python3
############################################################################################
# Main Processing of App
#
# This file is the meat of the API. The app is initialized, DB is accessed, and config files
# are loaded up. Note that it is in this file that user-defined config files are chosen,
# if they exist.
############################################################################################
import getpass
from flask import Flask
from version_1 import v1
from flask_jwt import JWT
from flask_mail import Mail
from authentication import *
from flask_cors import CORS
from db.models import User, Dog
from flask_security import Security
from flask_security.utils import encrypt_password

app = Flask(__name__)


#############################################
########## App Configuration
#############################################
app.config.from_object('config.base_settings')

# User Overrides
SETTINGS_BY_USERNAME = {
  'johnturner' : 'devel_user',
}

# Import the file if username matches
custom_settings_file = None
custom_settings_file = SETTINGS_BY_USERNAME.get(getpass.getuser().lower())

if custom_settings_file is not None:
    app.config.from_object('config.{}'.format(custom_settings_file))

#############################################
########## Set Up Flask-Mail Server
#############################################
mail = Mail(app)

#############################################
########## Blueprints
#############################################
app.register_blueprint(v1, url_prefix='/api/v1')


#############################################
########## Database
#############################################
from db.models import db, user_datastore
db.init_app(app)


#############################################
########## Security - Flask-Security and JWT
#############################################
security = Security(app, user_datastore)
jwt      = JWT(app, authenticate, load_user)

#############################################
########## Bootstrap Several Users
# https://github.com/graup/flask-restless-security/blob/master/server.py
#############################################
def create_test_models():
    # Create the default roles
    basic = user_datastore.find_or_create_role(name='User', description="Basic user")
    admin = user_datastore.find_or_create_role(name='Admin', description='API Administrator')

    # Create the default users
    user_datastore.create_user(email='test1@gmail.com', password=encrypt_password('testing123'), first_name="Test User", last_name="1")
    user_datastore.create_user(email='test2@gmail.com', password=encrypt_password('testing123'), first_name="Test User", last_name="2")
    user_datastore.create_user(email='test3@gmail.com', password=encrypt_password('testing123'), first_name="Test User", last_name="3")

    # Save users
    db.session.commit()

    # Activate users and assign roles
    user1 = user_datastore.find_user(email='test1@gmail.com')
    user2 = user_datastore.find_user(email='test2@gmail.com')
    user3 = user_datastore.find_user(email='test3@gmail.com')

    user_datastore.activate_user(user1)
    user_datastore.activate_user(user2)
    user_datastore.activate_user(user3)

    user_datastore.add_role_to_user(user1, admin)
    user_datastore.add_role_to_user(user2, basic)
    user_datastore.add_role_to_user(user3, basic)

    # Save changes
    db.session.commit()

    # Create a couple of dogs and tie them to owners
    dog       = Dog('Labrador')
    dog.owner = user2
    dog.add(dog)

    dog       = Dog('Great Dane')
    dog.owner = user2
    dog.add(dog)

    dog       = Dog('Husky')
    dog.owner = user3
    dog.add(dog)

@app.before_first_request
def bootstrap_app():
    if db.session.query(User).count() == 0:
        create_test_models()


#############################################
########## Run
#############################################
if __name__ == '__main__':
    app.run(host     = app.config['HOST'],
            debug    = app.config['DEBUG'],
            threaded = True,
            port     = app.config['PORT']
    )
