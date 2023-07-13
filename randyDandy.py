import json

json_file_path = 'responses.json'

with open(json_file_path) as file:
    data = json.load(file)