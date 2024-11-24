# Importing necessary modules
import os  # Provides functions to interact with the operating system
from pathlib import Path  # Helps in handling and manipulating file paths easily
import logging  # Used for tracking events that happen during program execution

# Setting up basic logging configuration to display timestamp and messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Defining the project name
project_name = "WineQuality"

# List of files and directories to be created for the project structure
list_of_files = [
    "",  # Base directory
    f"src/{project_name}/__init__.py",  # __init__.py file for the main project package
    f"src/{project_name}/components/__init__.py",  # Components module initializer
    f"src/{project_name}/utils/__init__.py",  # Utils module initializer
    f"src/{project_name}/utils/common.py",  # Common utility functions
    f"src/{project_name}/config/__init__.py",  # Config module initializer
    f"src/{project_name}/config/configuration.py",  # Configuration file
    f"src/{project_name}/pipeline/__init__.py",  # Pipeline module initializer
    f"src/{project_name}/entity/__init__.py",  # Entity module initializer
    f"src/{project_name}/entity/config_entity.py",  # Entity configuration file
    f"src/{project_name}/constants/__init__.py",  # Constants module initializer
    "config/config.yaml",  # Configuration YAML file
    "params.yaml",  # Parameters YAML file
    "schema.yaml",  # Schema file for data validation
    "main.py",  # Main script for running the project
    "app.py",  # Flask/Django web application file
    "Dockerfile",  # Docker configuration file
    "requirements.txt",  # Python dependencies list
    "setup.py",  # Project setup file for packaging
    "research/trials.ipynb",  # Jupyter notebook for research and trials
    "templates/index.html",  # HTML template for the app
    "test.py"  # Script for testing
]

# Iterating through each file path in the list
for filepath in list_of_files:
    # Converting the string path to a Path object for compatibility and easy handling
    filepath = Path(filepath)
    # Splitting the path into directory and file name
    filedir, filename = os.path.split(filepath)

    # If the directory path is not empty, create the directory (if it doesn't already exist)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directories as needed
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # If the file doesn't exist or is empty, create it
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Open the file in write mode
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")

    else:
        # Log that the file already exists
        logging.info(f"{filename} already exists")
