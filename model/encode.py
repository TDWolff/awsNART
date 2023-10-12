# models/encode.py
respond_list = ["Hello", "Hi", "Hey",]
respond_data = []

def initEncode():
    for item in respond_list:
        respond_data.append({"response": item})

def getResponses():
    return respond_data

# Call initEncode to initialize the responses
initEncode()
