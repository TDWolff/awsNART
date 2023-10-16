from flask import jsonify

respond_list = ["Hello", "Hi"]  # Initialize a list with default responses
respond_data = []  # Initialize a list to store the responses

def initEncode():
    for item in respond_list:
        respond_data.append({"response": item})

def getResponses():
    response = jsonify(respond_data)  # Get the Flask Response object
    data = response.get_json()  # Extract the JSON data from the Response object
    return jsonify(data)  # Return the JSON data as a JSON response

def addResponse(response):
    if response not in respond_list:  # Check if the response already exists in the list
        respond_list.append(response)  # Add the new response to the list
        respond_data.append({"response": response})  # Add the new response to the list
        return jsonify({'updating list': 'success', 'output': response, 'responses': respond_data})
    else:
        return jsonify({'updating list': 'failed', 'message': 'Response already exists in the list'})
