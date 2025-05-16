import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import os
from pathlib import Path
from src.data.fetch_data import load_config

def train_model():
    config = load_config()
    processed_data_path = config['paths']['processed_data']
    model_path = config['paths']['models']

    # Load Features
    df = pd.read_csv(os.path.join(processed_data_path, "features.csv"))
    X = df.drop('target_position', axis=1)
    y = df['target_position']

    # Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train XGBoost Model
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.2f}")

    # Save Model
    Path(model_path).mkdir(parents=True, exist_ok=True)
    joblib.dump(model, os.path.join(model_path, "xgboost_model.pkl"))
    print(f"Saved model to {model_path}/xgboost_model.pkl")

if __name__ == "__main__":
    train_model()