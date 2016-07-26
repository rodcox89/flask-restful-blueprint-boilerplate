from flask import Blueprint, abort, jsonify
from flask.ext import restful
from flask.ext.cors import CORS
from version_1.resources.hello_world.hello_world import HelloWorld

v1 = Blueprint('v1', __name__)

CORS(v1)

api = restful.Api()

api.init_app(v1)

@v1.route('/')
def show():
    return 'test'

api.add_resource(HelloWorld,  '/hello_world/<string:id>', '/hello_world')
