import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox object.
    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:ValueError: If the YAML file is not found.
    e:BoxValueError: If the YAML file is not valid.

    Returns:
        ConfigBox: A ConfigBox object containing the contents of the YAML file.
    """

    try:
        with open(path_to_yaml, "r") as f:
            content = yaml.safe_load(f)
            logger.info(f"Successfully read YAML file from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Invalid YAML file: {e}")
        raise ValueError(f"Invalid YAML file: {e}")
    except Exception as e:
        raise e


@ensure_annotations
def create_directory(path_to_directories: list, verbose: bool = True):
    """
    Creates a directory if it does not exist.
    Args:
        path_to_directories (list): A list of directories to create.
        verbose (bool): Whether to print a message when a directory is created.

    Raises:
        OSError: If a directory cannot be created.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")


@ensure_annotations
def get_size(path:Path)->str:
    """
    get size in KB

    Args:
        path (Path): path to file

    Returns:
        str: size in KB
    """

    size_in_kb=round(os.path.getsize(path)/1024)
    return f'{size_in_kb} KB'