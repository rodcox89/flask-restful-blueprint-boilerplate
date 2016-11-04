# coding: utf-8
############################################################################################
# Models For API
#
# This file holds all of the models for the API, used by SQLALchemy to create and maintain
# the PostgreSQL DB
############################################################################################
import pytz, datetime
from marshmallow import validate
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy
from marshmallow_jsonapi import Schema, fields
from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore

# Prepare the database
db = SQLAlchemy()

#############################################
########## Utility Classes/Constants
#############################################

# Class to add, update and delete data via SQLALchemy sessions
class CRUD():

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

# Create the validation for what we see as "not blank"
NOT_BLANK       = validate.Length(min=1, error='Field cannot be blank')
PASSWORD_LENGTH = validate.Length(min=10, error='Password too short')

#############################################
########## Models
#############################################

# https://pythonhosted.org/Flask-Security/quickstart.html
# Association Table for Roles and Users
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'

    id          = db.Column(db.Integer(), primary_key=True)
    name        = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<models.Role[name=%s]>' % self.name

class RoleSchema(Schema):

    # Validates for the different fields
    id          = fields.Integer(dump_only=True)
    name        = fields.String(validate=NOT_BLANK)
    description = fields.String(validate=NOT_BLANK)

    # Self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/roles/"
        else:
            self_link = "/roles/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'role'


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id               = db.Column(db.Integer, primary_key=True)
    email            = db.Column(db.String(255), unique=True)
    password         = db.Column(db.String(255))
    first_name       = db.Column(db.String(255))
    last_name        = db.Column(db.String(255))
    active           = db.Column(db.Boolean())
    confirmed_at     = db.Column(db.DateTime())
    last_login_at    = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip    = db.Column(db.String(255))
    current_login_ip = db.Column(db.String(255))
    login_count      = db.Column(db.Integer())

    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    dogs  = db.relationship('Dog', backref="owner")

    # http://docs.sqlalchemy.org/en/rel_1_0/orm/mapped_attributes.html#simple-validators
    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address

    def __repr__(self):
        return '<models.User[email=%s]>' % self.email

class UserSchema(Schema):

    # Validation for the different fields
    id               = fields.Integer(dump_only=True)
    email            = fields.String(validate=NOT_BLANK)
    password         = fields.String(load_only=True, validate=PASSWORD_LENGTH)
    first_name       = fields.String(validate=NOT_BLANK)
    last_name        = fields.String(validate=NOT_BLANK)
    active           = fields.Boolean(dump_only=True)
    confirmed_at     = fields.DateTime(dump_only=True)
    last_login_at    = fields.DateTime(dump_only=True)
    current_login_at = fields.DateTime(dump_only=True)
    last_login_ip    = fields.String(dump_only=True)
    current_login_ip = fields.String(dump_only=True)
    login_count      = fields.Integer(dump_only=True)

    roles = fields.Relationship(many=True,
                                include_resource_linkage=True,
                                type_='role',
                                schema='RoleSchema',
                                # related_url='/roles/{role_id}',
                                # related_url_kwargs={'role_id': '<role.id>'}
    )
    dogs  = fields.Relationship(many=True,
                                include_resource_linkage=True,
                                type_='dog',
                                schema='DogSchema',
                                # related_url='/dogs/{dog_id}',
                                # related_url_kwargs={'dog_id': '<dog.id>'}
    )

    # Self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/users/"
        else:
            self_link = "/users/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'user'


# https://pythonhosted.org/Flask-Security/quickstart.html
user_datastore = SQLAlchemyUserDatastore(db, User, Role)


class Dog(db.Model, CRUD):
    __tablename__ = 'dog'

    id           = db.Column(db.Integer, primary_key=True)
    dog_type     = db.Column(db.String, nullable=False, unique=True)
    date_created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    owner_id     = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, dog_type):
        self.dog_type = dog_type

    def __repr__(self):
        return '<models.Dog[dog_type=%s]>' % self.dog_type

class DogSchema(Schema):

    # Validation for the different fields
    id           = fields.Integer(dump_only=True)
    dog_type     = fields.String(validate=NOT_BLANK)
    date_created = fields.DateTime(dump_only=True)

    owner = fields.Relationship(related_url='/users/{user_id}',
                                related_url_kwargs={'user_id': '<owner_id>'},
                                many=False,
                                include_resource_linkage=True,
                                type_='user',
                                schema='UserSchema'
    )

    # Self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/dogs/"
        else:
            self_link = "/dogs/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'dog'
