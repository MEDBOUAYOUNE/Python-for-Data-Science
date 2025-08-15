# REF: https://pillow.readthedocs.io/en/stable/reference/Image.html#functions
# REF: https://numpy.org/doc/stable/reference/generated/numpy.asarray.html
# REF: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html

import numpy as np
from numpy import ndarray
from PIL import Image


def ft_load(path: str) -> ndarray:
    """
    Loads an image from the specified path and converts it to a NumPy array.
    Args:
        path (str): The file path to the image.
    Returns:
        ndarray: The image as a NumPy array.
    Raises:
        FileNotFoundError: If the image file does not exist.
        ValueError: If the image cannot be opened or converted.
    """
    try:
        assert isinstance(path, str), "Path must be a string"
        assert path.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')), "Unsupported image format"
        assert len(path) > 0, "Path cannot be empty"
        with Image.open(path) as image:
            print(f"Image mode: {image.mode}")
            imageNp = np.asarray(image)
            print(f"The shape of image is : {imageNp.shape}")
            return imageNp
    except FileNotFoundError as error:
        print(f"File not found: {error}")
    except ValueError as error:
        print(f"Value error: {error}")
    except AssertionError as error:
        print(f"Assertion error: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
