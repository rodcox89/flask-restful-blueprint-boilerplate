from flask import Blueprint, abort, jsonify
from flask.ext import restful
from flask.ext.cors import CORS
from version_1.resources.test.test import Test

v1 = Blueprint('v1', __name__)

CORS(v1)

api = restful.Api()

api.init_app(v1)

@v1.route('/')
def show():
    return 'test'

api.add_resource(Test,  '/test')
