import json

def fetch_data():
    with open('data/mock_sensor_data.json', 'r') as f:
        data = json.load(f)
    return data
