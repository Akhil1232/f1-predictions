import requests
import pandas as pd
import yaml
import os
from pathlib import Path
from src.utils import load_config

BASE_URL="https://api.openf1.org/v1"

def fetch_openf1_data(endpoint, params=None):
    base_url = BASE_URL
    url = f"{base_url}/{endpoint}"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def save_data(data, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(path, index=False)

def main():
    config = load_config()
    raw_data_path = config['paths']['raw_data']

    # Fetch Data for 2024 Season
    endpoints = [
        {"name": "sessions", "params": {"year": 2024}},
        {"name": "results", "params": {"year": 2024}},
        {"name": "drivers", "params": {}},
        {"name": "laps", "params": {"year": 2024}}
    ]

    for endpoint in endpoints:
        data = fetch_openf1_data(endpoint["name"], endpoint["params"])
        df = pd.DataFrame(data)
        filename = f"{endpoint['name']}_2024.csv"
        save_data(df, os.path.join(raw_data_path, filename))
        print(f"Saved data to {filename}")

if __name__ == "__main__":
    main()