# F1 Race Predictor
## Overview
This project is an end-to-end AI/ML pipeline for predicting Formula 1 race outcomes (e.g., driver finishing positions) using historical data from the OpenF1 API. Built with Python, it includes data fetching, preprocessing, feature engineering, model training with XGBoost, and deployment via FastAPI. The modular structure supports iterative improvements for adding advanced features like telemetry or weather data.

## Project Structure
```markdown
f1_race_predictor/
├── data/                   # Raw and processed data
├── notebooks/              # Jupyter notebooks for EDA
├── src/                    # Source code for data, features, models, and visualization
├── tests/                  # Unit tests
├── api/                    # FastAPI app for model deployment
├── configs/                # Configuration files
├── models/                 # Trained models
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── LICENSE                 # License file
├── .gitignore              # Git ignore file
├── setup.py                # Package setup
└── run.py                  # Pipeline entry point
```

## Setup

### Clone the Repository:
```python
git clone <repository-url>
cd f1_race_predictor
```


### Create a Virtual Environment:
```python
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies:
```python
pip install -r requirements.txt
```

## Configure Paths:

Update configs/config.yaml with paths for raw data, processed data, and models if needed.


## Usage

### Run the Pipeline:Fetch data, preprocess, build features, train the model, and visualize results:
```python
python run.py
```

### Run the API:Start the FastAPI server for predictions:
```python
python api/main.py
```

### Test the API:
```console
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"grid_position": 1, "driver_experience": 30, "avg_lap_time": 90.5}'
```


### Run Tests:
```python
pytest tests/
```



## Data Source

OpenF1 API: Provides historical F1 data (races, results, drivers, laps). No API key required. See api.openf1.org for details.

### Future Enhancements

Integrate telemetry data from OpenF1’s /car_data endpoint.
Add weather data via external APIs or scraping.
Implement advanced models (e.g., LSTM, ensemble methods).
Add CI/CD with GitHub Actions.

### Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/new-feature).
Commit changes (git commit -m "Add new feature").
Push to the branch (git push origin feature/new-feature).
Open a pull request.

License
MIT License (see LICENSE file).