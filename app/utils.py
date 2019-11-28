import errno
import os
from os.path import join
import json
from typing import Union, Type
from pathlib import Path

def make_dir(directory: Union[str, Type[Path]]) -> None:
    """Create a directory if does not exist.

    Arguments:
        directory: directory to create.
    """
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def read_json(input_file: Union[str, Type[Path]]) -> dict:
    with open(input_file, "r") as file:
        config = json.load(file)
    return config


def save_json(obj: Union[dict, list], output_file: Union[str, Type[Path]]) -> None:
    with open(output_file, "w") as file:
        json.dump(obj, file, indent=4)