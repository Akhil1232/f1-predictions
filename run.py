from src.data.fetch_data import main as fetch_data
from src.data.pre_process import main as preprocess_data
from src.features.build_features import main as build_features
from src.models.train_model import train_model
from src.visualization.visualize import plot_feature_importance

def main():
    print("Fetching Data...")
    fetch_data()
    print("Preprocessing Data...")
    preprocess_data()
    print("Building Features...")
    build_features()
    print("Training Model")
    train_model()
    print("Visualizing Results...")
    plot_feature_importance()

if __name__ == "__main__":
    main()
    
