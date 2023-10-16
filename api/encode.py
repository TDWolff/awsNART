from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from model.encode import *


encode_api = Blueprint('encode_api', __name__, url_prefix='/api/encode')
api = Api(encode_api)

class EncodeAPI():
    class _Read(Resource):
            def get(self):
                try:
                    responses = getResponses()
                    response_list = [r['response'] for r in responses]
                    return jsonify(response_list)
                except Exception as e:
                    return {'response': 'error', 'message': str(e)}


    class _Write(Resource):
        def post(self):
            try:
                data = request.get_json()
                response = data.get('userInput')
                addResponse(response)  # Call addResponse in model/encode.py to add the response to the respond_list
                return {'sent to model': 'success', 'output': response, 'responses': respond_data}
            except Exception as e:
                print('Error adding response:', e)
                return {'response': 'error', 'message': str(e)}

api.add_resource(EncodeAPI._Read, '/')
api.add_resource(EncodeAPI._Write, '/write')

if __name__ == "__main__": 
    import requests
    from flask import request

    server = request.host_url.rstrip('/') # get the URL of the server dynamically
    url = server + "/api/encode"
    print(url)

    response = requests.get(url+"/")  # read responses by id
    print(response)
    try:
        print(response.json())
    except:        print("unknown error")

