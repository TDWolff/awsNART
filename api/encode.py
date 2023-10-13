from flask import Blueprint, jsonify, request  # Import 'request' from 'flask'
from flask_restful import Api, Resource
import requests
import random
from model.encode import *

encode_api = Blueprint('encode_api', __name__, url_prefix='/api/encode')
api = Api(encode_api)

class EncodeAPI():
    class _Read(Resource):
        def get(self):
            return jsonify(getResponses())

    class _Write(Resource):
        def post(self):
            try:
                data = request.get_json()
                response = data.get('userInput')  # Correctly access the 'userInput' key
                addResponse(response)
                respond_list.append(response)  # Add the response to the respond_list list
                return {'response': 'success', 'respond_list': respond_list}  # Return a JSON response indicating success and the updated respond_list
            except Exception as e:
                print('Error adding response:', e)
                return {'response': 'error', 'message': str(e)}  # Return a JSON response with an error message

api.add_resource(EncodeAPI._Read, '/')  # Add the correct resource classes
api.add_resource(EncodeAPI._Write, '/write')


if __name__ == "__main__": 
    import requests
    from flask import request

    server = request.host_url.rstrip('/') # get the URL of the server dynamically
    url = server + "/api/encode"
    responses = []  # responses list
    print(url)

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