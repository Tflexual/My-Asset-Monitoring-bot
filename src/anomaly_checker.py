import json


def check_anomalies(data):
    with open('config/thresholds.json', 'r') as f:
        thresholds = json.load(f)

    anomalies = []
    for record in data:
        if not (thresholds['temperature']['min'] <= record['temperature'] <= thresholds['temperature']['max']):
            anomalies.append(f"Temperature anomaly detected at {record['timestamp']}")
        if not (thresholds['humidity']['min'] <= record['humidity'] <= thresholds['humidity']['max']):
            anomalies.append(f"Humidity anomaly detected at {record['timestamp']}")

    print(f"Anomalies detected: {anomalies}")  # Debugging print
    return anomalies

