from flask import Blueprint, jsonify, request  # Import 'request' from 'flask'
from flask_restful import Api, Resource
import requests
import random
import csv
from model.encode import *
import json

encode_api = Blueprint('encode_api', __name__, url_prefix='/api/encode')
api = Api(encode_api)

class EncodeAPI():
    class _Read(Resource):
        def get(self):
            with open('./data/userresponses.csv', mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                responses = [{'response': row['response']} for row in csv_reader]
            return jsonify(responses)

    class _Write(Resource):
        def post(self):
            try:
                data = request.get_json()
                response = data.get('userInput')
                with open('./data/userresponses.csv', mode='a', newline='') as csv_file:
                    fieldnames = ['response']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writerow({'response': response})
                return {'response': 'success'}
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