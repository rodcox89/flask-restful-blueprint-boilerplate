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
from flask.ext.cors import CORS

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
########## Blueprints
#############################################
app.register_blueprint(v1, url_prefix='/api/v1')


#############################################
########## Database
#############################################
from db.models import db
db.init_app(app)


#############################################
########## Run
#############################################
if __name__ == '__main__':
    app.run(host     = app.config['HOST'],
            debug    = app.config['DEBUG'],
            threaded = True,
            port     = app.config['PORT']
    )
