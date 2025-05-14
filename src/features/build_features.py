import pandas as pd
from src.data.fetch_data import load_config
import os

def build_features(df):
    # Basic Features
    df['grid_position'] = df['starting_grid'].astype(int) if 'starting_grid' in df.columns else 999
    df['driver_experience'] = df['date_start'].dt.year - pd.to_datetime(df['date_of_birth']).dt.year
    df['avg_lap_time'] = df.groupby('driver_number')['lap_time'].transform('mean')

    # Target Variable finishing position
    df['target_position'] = df['position'].astype(int)

    # Select Features
    features = ['grid_position', 'driver_experience', 'avg_lap_time']
    return df[features + ['target_position']]

def main():
    config = load_config()
    processed_data_path = config['paths']['processed_data']
    df = pd.read_csv(os.path.join(processed_data_path, "processed-data.csv"))
    feature_df = build_features(df)
    feature_df.to_csv(os.path.join(processed_data_path, "features.csv"), index=False)
    print("Saved features to features.csv")

if __name__ == "__main__":
    main()
    