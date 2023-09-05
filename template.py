import os
from pathlib import Path
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Get the directory of the current script (where template.py is located)
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the base directory where the files and directories should be created
base_directory = script_directory

# List of files and directories to create
list_of_files = [
    "data/dummy.csv",  
    "utils/__init__.py",
    "utils/data_ingestion.py",
    "utils/data_cleaning.py",
    "utils/model_development.py",
    "log/__init__.py",
    "config/__init__.py",
    "config/configuration.py",
    "pipelines/__init__.py",
    "pipelines/deployment_pipeline.py",
    "pipelines/training_pipeline.py",
    "pipelines/data_ingestion_pipeline.py",
    "pipelines/data_cleaning_pipeline.py",
    "steps/__init__.py",
    "steps/data_ingestion.py",
    "steps/data_cleaning.py",
    "steps/model_training.py",
    "steps/model_evaluation.py",
    "saved_model/dummy.pkl",  
    "test/__init__.py",
    "params.yaml",
    "__init__.py",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

# Loop through the list of files and directories
for item in list_of_files:
    # Construct the full path for the item
    item_path = Path(os.path.join(base_directory, item))
    filedir, filename = os.path.split(item_path)
    
    # Create directories if needed
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the item {filename}")
    
    # Create empty files if needed
    if not item.endswith('/'):
        if (not os.path.exists(item_path)) or (os.path.getsize(item_path) == 0):
            open(item_path, 'w').close()  # Create an empty file
            logging.info(f"Creating empty file: {item_path}")
        else:
            logging.info(f"{filename} already exists")

logging.info("Code execution completed.")
