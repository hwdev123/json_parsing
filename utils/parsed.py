import json


def json_data():
    with open("data.json", "r") as f:
        json_file = json.load(f)
        return json_file
    

if __name__ == '__main__':
    json_data()