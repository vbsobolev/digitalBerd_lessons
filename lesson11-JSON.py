import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)
print(json_object)
print(type(json_object))

# Writing to sample.json
with open(r'files\sample.json', 'w') as outfile:
    json.dump(dictionary, outfile)
    # outfile.write(json_object)

# Reading JSON file
with open(r'files\sample.json', 'r') as openfile:
    json_object = json.load(openfile)
print(json_object)
print(type(json_object))
