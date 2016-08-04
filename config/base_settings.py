############################################################################################
# Global Configurations - Base
#
# This file holds base global configurations for the API. In order to accomodate for
# multiple developers working on this project, this base config file is set up in order to
# have certain settings (production settings) be default. After those default settings are
# put into place, a check is made on the name of the user running the code, in the main.py
# file, and if it matches explicitly-declared users, the settings can be overridden by user-
# defined files that are housed in this same directory.
############################################################################################

from datetime import timedelta

#############################################
########## Base (Production) Settings
#############################################

# Flask Core Settings
APP_NAME   = "DogTracker"
DEBUG      = False
HOST       = '127.0.0.1'
PORT       = 5000
SECRET_KEY = "SOME SECRET"


# Database Settings
DB_USER = 'dog_dev'
DB_PASS = 'dog_dev'
DB_HOST = 'localhost'
DB_NAME = 'dog_dev_db'

SQLALCHEMY_DATABASE_URI = 'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'.format(
                            DB_USER=DB_USER,
                            DB_PASS=DB_PASS,
                            DB_HOST=DB_HOST,
                            DB_NAME=DB_NAME)


# Mail Settings
MAIL_SERVER   = 'smtp.example.com'
MAIL_PORT     = 465
MAIL_USE_SSL  = True
MAIL_USERNAME = 'username'
MAIL_PASSWORD = 'password'


# Security Settings
# https://pythonhosted.org/Flask-Security/configuration.html
# https://pythonhosted.org/Flask-JWT/
JWT_EXPIRATION_DELTA           = timedelta(days=30)
JWT_AUTH_URL_RULE              = '/api/v1/auth'
JWT_AUTH_USERNAME_KEY          = 'ownername'
JWT_AUTH_PASSWORD_KEY          = 'ownerpassword'
SECURITY_CONFIRMABLE           = True
SECURITY_TRACKABLE             = True
SECURITY_REGISTERABLE          = True
SECURITY_RECOVERABLE           = True
SECURITY_PASSWORD_HASH         = 'sha512_crypt'
SECURITY_PASSWORD_SALT         = 'add_salt'
SQLALCHEMY_TRACK_MODIFICATIONS = False
