from typing import Any
import logging
import json

logger = logging.getLogger(__name__)

def load_json_file(file_path: str) -> dict[str, Any]:
    # NOTE: could optimize this with batch processing
    """
    Load a JSON file from the given file path.

    Args:
        file_path: The path to the JSON file.

    Returns:
        A dictionary representing the loaded JSON data.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in file: {file_path} - {e}")
        raise

def save_json_file(file_path: str, data: dict[str, Any]) -> None:
    """
    Save a dictionary to a JSON file at the given file path.

    Args:
        file_path: The path to the JSON file.
        data: The dictionary to save.

    Raises:
        Exception: If an error occurs while writing the file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        logger.error(f"Error writing to file: {file_path} - {e}")
        raise

def camel_case_to_snake_case(input_str: str) -> str:
    """
    Convert a camelCase string to snake_case.

    Args:
        input_str: The string to convert.

    Returns:
        The converted string.
    """
    query_result = ""
    for i, char in enumerate(input_str):
        if char.isupper() and i > 0:
            result += "_"
        result += char.lower()
    return result

from src.config import Config

def get_config() -> Config:
    """
    Get the application configuration.

    Returns:
        The application configuration.
    """
    return Config()