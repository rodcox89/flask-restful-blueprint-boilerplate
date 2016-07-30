from flask.ext import restful
from flask.ext.cors import CORS
from version_1.resources.dog import DogList
from flask import Blueprint, abort, jsonify

# Declare the blueprint
v1 = Blueprint('v1', __name__)

# Set up cross-scripting allowed
CORS(v1)

# Set up the API and init the blueprint
api = restful.Api()
api.init_app(v1)

# Set the default route
@v1.route('/')
def show():
    return 'Hello World'

# Add resources - Can include multiple routes
api.add_resource(DogList, '/dogs/<int:id>', '/dogs')
