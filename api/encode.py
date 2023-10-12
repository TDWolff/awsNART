from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random
from model.encode import *

encode_api = Blueprint('encode_api', __name__,
                   url_prefix='/api/encode')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(encode_api)

class EncodeAPI():
    class _Read(Resource):
        def get(self):
            return jsonify(getResponses())
    class _Write(Resource):
        def post(self):
            try:
                data = request.get_json()
                user_input = data.get('userInput')

                # Now you can process 'user_input' as needed
                # For example, you can append it to the response list
                respond_data.append(user_input)

                # Return a JSON response with the updated response list
                return jsonify({'responses': respond_data})

            except Exception as e:
                return jsonify({'error': 'Invalid JSON data'}), 400


    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Read, '/')
    api.add_resource(_Write, '/write')


if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://nartbackend.nighthawkcodingsociety.com' # run from web
    url = server + "/api/encode"
    responses = []  # responses list

    responses.append(
        requests.get(url+"/")  # read responses by id
        )

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")