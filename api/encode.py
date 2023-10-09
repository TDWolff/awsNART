import base64
import json

# Get user input as a string
user_input = input("Enter a string: ")

# Encode the user input to bytes
user_input_bytes = user_input.encode('utf-8')

# Encode the bytes in Base64
user_input_base64 = base64.b64encode(user_input_bytes).decode('utf-8')

# Create a dictionary to hold the encoded value
data = {'encoded_string': user_input_base64}

# Convert the dictionary to a JSON string
json_data = json.dumps(data)

# Print the JSON data
print(json_data)
