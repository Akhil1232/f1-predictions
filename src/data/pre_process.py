import pandas as pd
import os
from pathlib import Path
from src.utils import load_config

# Load Raw Data and Convert into Data frames using Pandas

def load_raw_data(raw_data_path):
    """
    This function will convert the Raw Data stored in .csv files into dataframes.

    Parameters:
    raw_data_path: Path to the Raw Data.
    """
    dataframes = {}
    for file in Path(raw_data_path).glob("*.csv"):
        dataframes[file.stem] = pd.read_csv(file)
    return dataframes

def preprocess_data(dataframes, processed_data_path):
    """
    In this function, we will get the data in the form of dataframes and combines it to perform analysis.
    
    Parameters:
    data_frames: The Data converted to dataframes from the csv.
    processed_data_path: Path to store the processed data.
    """
    # Load Datasets
    results = dataframes.get('result_2024')
    sessions = dataframes.get('sessions_2024')
    drivers = dataframes.get('drivers_2024')
    laps = dataframes.get('laps_2024')

    # Merge Datasets
    merged_data = results.merge(sessions, on='session_key', how='left')
    merged_data = merged_data.merge(drivers, on="drivers_key", how='left')
    merged_data = merged_data.merge(laps, on=['session_key', 'driver_number'], how='left')

    # Handle missing values
    # merged_data.fillna()

    # Convert Data Types because by default the data is in Text format need to convert to standard datetime64 format
    merged_data['date_start'] = pd.to_datetime(merged_data['date_start'])

    # Save Processed Data
    Path(processed_data_path).mkdir(parents=True, exist_ok=True)
    output_path = os.path.join(processed_data_path, "processed_data.csv")
    merged_data.to_csv(output_path, index=False)
    print(f"Saved processed data to {output_path}")
    return merged_data

def main():
    config = load_config()
    raw_data_path = config['paths']['raw_data']
    processed_data_path = config['paths']['processed_data']
    dataframes = load_raw_data(raw_data_path)
    preprocess_data(dataframes, processed_data_path)

if __name__ == "__main__":
    main()