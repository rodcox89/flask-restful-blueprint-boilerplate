from flask import jsonify
from flask_restful import Resource
import json

dogs = ['mini', 'medium', 'big']



class HelloWorld(Resource):
    def get(self):
        # Route used to return objects

        return dogs

    def put(self, id):
        # route used to update or edit an object
        return id

    def post(self):
        # route used to create a new object
        return 'post'
    def delete(self, id):
        # route used to delete an object
        return 'delete'
