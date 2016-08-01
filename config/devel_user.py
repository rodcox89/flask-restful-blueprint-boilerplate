############################################################################################
# Template for User-Specific Configuration
#
# Here a developer can specify machine-specific settings to override the base settings
# found in the base_settings.py file of the config directory.
#
# NOTE: If someone is going to declare specific settings here, he/she will need to make sure
# to add the corresponding unix username (or change how settings are imported) to the
# main.py file in order to make sure that the settings are overriden.
############################################################################################

from datetime import timedelta

#############################################
########## User-Level Settings
#############################################

# Flask Core Settings
APP_NAME   = "DogTracker"
DEBUG      = True
HOST       = 'localhost'
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
# # https://pythonhosted.org/Flask-Security/configuration.html
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
