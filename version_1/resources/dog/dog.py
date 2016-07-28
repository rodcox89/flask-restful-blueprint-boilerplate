from flask import jsonify
from flask_restful import Resource, reqparse
import json

# The "Model"
DOGS = {
    '0': {'type': 'mini'},
    '1': {'type': 'medium'},
    '2': {'type': 'big'},
}

# Set up the request argument parser
parser = reqparse.RequestParser()
parser.add_argument('type')

class Dog(Resource):

    def get(self, id=None):
        # If ID is passed in, then return a single dog type
        if id:
            try:
                return DOGS[id]
            except Exception:
                pass
        # Otherwise just return the entire list
        return DOGS

    def put(self, id):
        # Route used to update or edit an object
        return id

    def post(self):
        # Route used to create a new object
        # Get the argument passed in (should be "type"), and create new dog
        args         = parser.parse_args()
        dog_id       = str(int(max(DOGS.keys())) + 1)
        DOGS[dog_id] = {'type': args['type']}

        return DOGS[dog_id], 201

    def delete(self, id):
        # route used to delete an object
        return 'delete'
