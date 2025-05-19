import pytest 
import pandas as pd
from src.data.pre_process import preprocess_data, load_raw_data

def test_preprocess():
    # Mock Data
    dataframes = {
        'result_2024': pd.DataFrame({'session_key': [1], 'driver_number': [1], 'position': [1]}),
        'session_2024': pd.DataFrame({'session_key': [1], 'date_start': ['2024-03-01']}),
        'drivers_2024': pd.DataFrame({'driver_number': [1], 'date_of_birth': ['1990-01-01']}),
        'laps_2024': pd.DataFrame({'session_key': [1], 'driver_number': [1], 'lap_time': [90.5]})
    }
    processed_data_path = "data/processed/test/"
    df = preprocess_data(dataframes, processed_data_path)
    assert 'position' in df.columns
    assert df['start_date'].dtype == 'datetime64[ns]'
