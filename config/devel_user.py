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

#############################################
########## User-Level Settings
#############################################
DEBUG = True

HOST = 'localhost'

PORT = 5000

SECRET_KEY = "SOME SECRET"

DB_USER = 'dog_dev'
DB_PASS = 'dog_dev'
DB_HOST = 'localhost'
DB_NAME = 'dog_dev_db'

SQLALCHEMY_DATABASE_URI = 'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'.format(
                            DB_USER=DB_USER,
                            DB_PASS=DB_PASS,
                            DB_HOST=DB_HOST,
                            DB_NAME=DB_NAME)
