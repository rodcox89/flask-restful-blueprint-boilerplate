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
from db.models import User
from flask_mail import Mail
from authentication import *
from flask.ext.cors import CORS
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
    user_datastore.create_user(email='test@gmail.com', password=encrypt_password('test'))
    user_datastore.create_user(email='test2@gmail.com', password=encrypt_password('test2'))
    db.session.commit()

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
