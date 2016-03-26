from flask import jsonify
from flask_restful import Resource
import json

dogs = ['mini', 'medium', 'big']



class Test(Resource):
    def get(self):

        return dogs

    def put(self, id):

        return id

    def post(self):

        return 'post'
    def delete(self):

        return 'delete'
