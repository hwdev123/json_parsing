import json

def json_data():
    with open("data.json", "r") as f:
        json_file = json.load(f)
        return json_file