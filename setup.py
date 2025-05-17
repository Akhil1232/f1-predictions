from setuptools import setup, find_packages

setup(
    name="f1-predictions",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas==2.2.3",
        "numpy==2.1.2",
        "requests==2.32.3",
        "scikit-learn==1.5.2",
        "xgboost==2.1.1",
        "matplotlib==3.9.2",
        "seaborn==0.13.2",
        "fastapi==0.115.4",
        "uvicorn==0.32.0",
        "pytest==8.3.3",
        "python-dotenv==1.0.1",
        "pyyaml==6.0.2",
    ],
)