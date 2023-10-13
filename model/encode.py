import csv

# models/encode.py
respond_list = ["Hello", "Hi", "Hey",]
respond_data = []

def initEncode():
    for item in respond_list:
        respond_data.append({"response": item})

def getResponses():
    return respond_data

def addResponse(response):
    with open('./data/userresponses.csv', mode='a', newline='') as csv_file:
        fieldnames = ['response']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'response': response})
        respond_data.append({"response": response})
        return respond_data[-1]

# Call initEncode to initialize the responses
initEncode()
# models/encode.py

def initEncode():
    with open('./data/userresponses.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            respond_data.append({"response": row["response"]})

def getResponses():
    return respond_data

def addResponse(response):
    with open('userresponses.csv', mode='a') as csv_file:
        fieldnames = ['response']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'response': response})
        respond_data.append({"response": response})
        return respond_data[-1]

respond_data = []
initEncode()
