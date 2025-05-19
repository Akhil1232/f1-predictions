import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib
from src.utils import load_config

def plot_feature_importance():
    config = load_config()
    model_path = config['paths']['models']
    model = joblib.load(os.path.join(model_path, "xgboost_model.pkl"))

    #Feature Importance
    importance = model.feature_importances_
    features = model.feature_names_in_
    df_importance = pd.DataFrame({'Feature': features, 'Importance': importance})
    df_importance = df_importance.sort_values('Importance', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Importnace', y='Feature', data=df_importance)
    plt.title('Feature Importance')
    plt.savefig('feature_importance.png')
    plt.close()

if __name__ == "__main__":
    plot_feature_importance()