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

#############################################
########## Base (Production) Settings
#############################################
DEBUB = False

HOST = '127.0.0.1'

PORT = 5000

SECRET_KEY = "SOME SECRET"

DB_USER = 'dog_dev'
DB_PASS = 'dog_dev'
DB_ADDR = 'localhost'
DB_NAME = 'dog_dev_db'

SQLALCHEMY_DATABASE_URI = 'postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}'.format(
                            DB_USER=DB_USER,
                            DB_PASS=DB_PASS,
                            DB_ADDR=DB_ADDR,
                            DB_NAME=DB_NAME
                        )
