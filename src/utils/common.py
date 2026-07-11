import os
import sys
import yaml
import json
import joblib
import numpy as np

from src.logger.logger import logger
from src.exception.exception import CustomException


def read_yaml(file_path: str) -> dict:
    """
    Read YAML file and return dictionary.
    """
    try:
        with open(file_path, "r") as yaml_file:
            logger.info(f"Reading YAML file: {file_path}")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        logger.error(CustomException(e, sys))
        raise CustomException(e, sys)


def create_directories(paths: list):
    """
    Create multiple directories.
    """
    try:
        for path in paths:
            os.makedirs(path, exist_ok=True)

        logger.info("Directories created successfully.")

    except Exception as e:
        logger.error(CustomException(e, sys))
        raise CustomException(e, sys)


def save_object(file_path: str, obj):
    """
    Save Python object.
    """
    try:
        joblib.dump(obj, file_path)
        logger.info(f"Object saved at: {file_path}")

    except Exception as e:
        logger.error(CustomException(e, sys))
        raise CustomException(e, sys)


def load_object(file_path: str):
    """
    Load Python object.
    """
    try:
        logger.info(f"Loading object from: {file_path}")
        return joblib.load(file_path)

    except Exception as e:
        logger.error(CustomException(e, sys))
        raise CustomException(e, sys)


def save_json(file_path: str, data: dict):
    """
    Save JSON file.
    """
    try:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

        logger.info(f"JSON saved at: {file_path}")

    except Exception as e:
        logger.error(CustomException(e, sys))
        raise CustomException(e, sys)


def load_json(file_path: str):
    """
    Load JSON file.
    """
    try:
        with open(file_path, "r") as json_file:
            logger.info(f"Loading JSON: {file_path}")
            return json.load(json_file)

    except Exception as e:
        logger.error(CustomException(e, sys))
        raise CustomException(e, sys)


def save_numpy_array(file_path: str, array: np.ndarray):
    """
    Save NumPy array.
    """
    try:
        np.save(file_path, array)
        logger.info(f"NumPy array saved at: {file_path}")

    except Exception as e:
        logger.error(CustomException(e, sys))
        raise CustomException(e, sys)


def load_numpy_array(file_path: str):
    """
    Load NumPy array.
    """
    try:
        logger.info(f"Loading NumPy array: {file_path}")
        return np.load(file_path, allow_pickle=True)

    except Exception as e:
        logger.error(CustomException(e, sys))
        raise CustomException(e, sys)