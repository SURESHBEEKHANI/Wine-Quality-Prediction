import os  # Module to interact with the operating system
from box.exceptions import BoxValueError  # Exception class for Box-related errors
import yaml  # Module for working with YAML files
from WineQuality import logger  # Custom logger for the project
import json  # Module for working with JSON files
import joblib  # Module for saving/loading binary files
from ensure import ensure_annotations  # Decorator for enforcing function annotations
from box import ConfigBox  # Enhanced dictionary-like object from Box
from pathlib import Path  # Module for working with file system paths
from typing import Any  # Generic type hint for any type


# In-memory cache for YAML files
_yaml_cache = {}


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: If any other error occurs during file reading.

    Returns:
        ConfigBox: A ConfigBox object containing the parsed YAML data.
    """
    global _yaml_cache
    if path_to_yaml in _yaml_cache:
        logger.info(f"yaml file: {path_to_yaml} retrieved from cache")
        return _yaml_cache[path_to_yaml]

    try:
        # Open and load the YAML file safely
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)  # Parse YAML content
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")  # Log success
            config = ConfigBox(content)  # Convert content to ConfigBox
            _yaml_cache[path_to_yaml] = config  # Cache the loaded content
            return config
    except BoxValueError:
        # Raise an error if the YAML file is empty
        raise ValueError("yaml file is empty")
    except Exception as e:
        # Log unexpected exceptions for debugging
        logger.error(f"Error reading YAML file at {path_to_yaml}: {e}")
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories if they do not exist.

    Args:
        path_to_directories (list): List of paths to directories to be created.
        verbose (bool, optional): If True, logs the creation of each directory. Defaults to True.
    """
    for path in path_to_directories:
        if not os.path.exists(path):  # Only attempt creation if directory doesn't exist
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Created directory at: {path}")
        elif verbose:
            logger.info(f"Directory already exists at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary as a JSON file.

    Args:
        path (Path): Path where the JSON file will be saved.
        data (dict): Data to be saved as JSON.
    """
    # Open the file in write mode and save data as JSON
    with open(path, "w") as f:
        json.dump(data, f, indent=4)  # Save JSON with indentation for readability
    logger.info(f"JSON file saved at: {path}")  # Log the save operation


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file and returns its content as a ConfigBox object.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: A ConfigBox object containing the parsed JSON data.
    """
    # Open and read the JSON file
    with open(path) as f:
        content = json.load(f)  # Load JSON content
    logger.info(f"JSON file loaded successfully from: {path}")  # Log success
    return ConfigBox(content)  # Return content as a ConfigBox object


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data as a binary file using joblib.

    Args:
        data (Any): Data to be saved as a binary file.
        path (Path): Path where the binary file will be saved.
    """
    # Save data to the binary file using joblib
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")  # Log the save operation


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Data retrieved from the binary file.
    """
    # Load data from the binary file using joblib
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")  # Log success
    return data  # Return the loaded data


@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in an appropriate unit.

    Args:
        path (Path): Path to the file.

    Returns:
        str: File size in an appropriate unit (bytes, KB, or MB).
    """
    size_in_bytes = os.path.getsize(path)
    if size_in_bytes < 1024:
        return f"{size_in_bytes} bytes"
    elif size_in_bytes < 1024 ** 2:
        return f"~ {size_in_bytes / 1024:.2f} KB"
    else:
        return f"~ {size_in_bytes / (1024 ** 2):.2f} MB"
