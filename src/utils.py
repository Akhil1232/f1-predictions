import yaml
import os

def load_config(config_path="configs/config.yaml"):
    """
    Load configuration from a YAML file.
    
    Args:
        config_path (str): Path to the configuration file.
        
    Returns:
        dict: Configuration dictionary
    """
    config_path = os.path.join(os.path.dirname(__file__), '..', config_path)
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)