from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
import os
from src.data.fetch_data import load_config

app = FastAPI()

# Load Model
config = load_config()
model_path = config['paths']['models']
model = joblib.load(os.path.join(model_path, "xgboost_model.pkl"))

class PredictionInput(BaseModel):
    grid_position: int
    driver_experience: int
    avg_lap_time: int

@app.post("/predict")
async def predict(input: PredictionInput):
    data = pd.DataFrame([input.dict()])
    prediction = model.predict(data)[0]
    return {"predicted_position": float(prediction)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    