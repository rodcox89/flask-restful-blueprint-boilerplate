# coding: utf-8
############################################################################################
# Models For API
#
# This file holds all of the models for the API, used by SQLALchemy to create and maintain
# the PostgreSQL DB
############################################################################################
import pytz, datetime
from marshmallow import validate
from flask.ext.sqlalchemy import SQLAlchemy
from marshmallow_jsonapi import Schema, fields

# Prepare the database
db = SQLAlchemy()

#############################################
########## Utility Classes
#############################################

#Class to add, update and delete data via SQLALchemy sessions
class CRUD():

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

#############################################
########## Models
#############################################

class Dog(db.Model, CRUD):
    id           = db.Column(db.Integer, primary_key=True)
    dog_type     = db.Column(db.String, nullable=False, unique=True)
    date_created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, dog_type):
        self.dog_type = dog_type

class DogSchema(Schema):

    # Create the validation for what we see as "not blank"
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    # Validation for the different fields
    id        = fields.Integer(dump_only=True)
    dog_type  = fields.String(validate=not_blank)


    # Self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/dogs/"
        else:
            self_link = "/dogs/{}".format(data['id'])
        return {'self': self_link}


    class Meta:
        type_ = 'dog'
