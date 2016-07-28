from flask import Blueprint, abort, jsonify
from flask.ext import restful
from flask.ext.cors import CORS
from version_1.resources.dog.dog import Dog

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
    return 'test'

# Add resources - Can include multiple routes
api.add_resource(Dog,
    '/dog/<string:id>',
    '/dog',
)
