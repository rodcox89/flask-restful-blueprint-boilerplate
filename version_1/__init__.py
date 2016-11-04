from flask_cors import CORS
from flask_restful import Api
from flask import Blueprint, abort, jsonify
from version_1.resources.dog import DogList, DogUpdate
from version_1.resources.role import RoleList, RoleUpdate
from version_1.resources.user import UserList, UserUpdate

# Declare the blueprint
v1 = Blueprint('v1', __name__)

# Set up cross-scripting allowed
CORS(v1)

# Set up the API and init the blueprint
api = Api()
api.init_app(v1)

# Set the default route
@v1.route('/')
def show():
    return 'Hello World'

#############################################
########## Resources to Add
#############################################

# Dogs
api.add_resource(DogList, '/dogs')
api.add_resource(DogUpdate, '/dogs/<int:id>')

# Users
api.add_resource(UserList, '/users')
api.add_resource(UserUpdate, '/users/<int:id>')

# Roles
api.add_resource(RoleList, '/roles')
api.add_resource(RoleUpdate, '/roles/<int:id>')
