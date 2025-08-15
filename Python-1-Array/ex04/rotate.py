# Source: https://stackoverflow.com/questions/69994725/how-to-reshape-numpy-arrays-to-turn-rows-into-columns
from load_image import ft_load
from PIL import Image
import numpy as np


def rotate(path: str) -> None:
    """
    Rotates an image by transposing the pixel values and saves the rotated image.
    Args:
        path (str): The file path to the image.
        Returns:
        None
        Raises:
            FileNotFoundError: If the image file does not exist.
            ValueError: If the image cannot be opened or converted.
    """
    try:
        _ndarray = ft_load(path)
        print(_ndarray)
        print(f"Original shape: {_ndarray.shape}")
        _ndarray = _ndarray[150:550, 400:800, 1]
        print(f"New shape after slicing: {_ndarray.shape}")
        columns = rows = 400

        transposed = np.zeros([columns, rows], dtype=np.uint8)
        for y in range(rows):
            for x in range(columns):
                transposed[y, x] = _ndarray[x, y]
        print(f"New shape after Transpose:: {transposed.shape}")
        print(transposed)
        # Before see the subject requirement, I was thinking to use reshape and transpose
        # _ndarray = _ndarray.reshape(400, 400).transpose()
        # print(f"New shape after Transpose:: {_ndarray.shape}")
        # print(_ndarray)
        new_image = Image.fromarray(transposed)
        new_image.save("rotated.jpg")
        new_image.show()
    except FileNotFoundError as error:
        print(f"File not found: {error}")
    except ValueError as error:
        print(f"Value error: {error}")
    except AssertionError as error:
        print(f"Assertion error: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


def main():
    """ """
    try:
        rotate("animal.jpeg")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
