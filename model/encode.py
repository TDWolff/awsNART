import json
from flask import jsonify

RESPONSES_FILE = 'responses.json'  # File to store the responses

respond_data = []  # Initialize a list to store the responses

def initEncode():
    global respond_data
    try:
        with open(RESPONSES_FILE, 'r') as f:
            respond_data = json.load(f)  # Load the responses from the file
    except FileNotFoundError:
        return jsonify({'init': 'failed', 'message': 'File not found'})

def saveResponses():
    with open(RESPONSES_FILE, 'w') as f:
        json.dump(respond_data, f)  # Save the responses to the file

def getResponses():
    response = jsonify(respond_data)  # Get the Flask Response object
    data = response.get_json()  # Extract the JSON data from the Response object
    return jsonify(data)  # Return the JSON data as a JSON response

def addUsername(response):
    global respond_data
    if response not in [r['response'] for r in respond_data]:  # Check if the response already exists in the list
        respond_data.append({"response": response})  # Add the new response to the list
        saveResponses()  # Save the updated responses to the file
        return jsonify({'updating list': 'success', 'output': response, 'responses': respond_data})
    else:
        return jsonify({'updating list': 'failed', 'message': 'Response already exists in the list'})
    
def addPassword(response):
    global respond_data
    if response not in [r['response'] for r in respond_data]:  # Check if the response already exists in the list
        respond_data.append({"response": response})  # Add the new response to the list
        saveResponses()  # Save the updated responses to the file
        return jsonify({'updating list': 'success', 'output': response, 'responses': respond_data})
    else:
        return jsonify({'updating list': 'failed', 'message': 'Response already exists in the list'})
