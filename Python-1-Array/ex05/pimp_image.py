
import numpy as np
from numpy import ndarray
from PIL import Image


def ft_invert(array: ndarray) -> ndarray:
    """Invert the colors of the image."""
    # Invert the colors by subtracting each channel from 255
    inverted_array = 255 - array
    new_image = Image.fromarray(inverted_array)
    new_image.save("inverted.jpg")
    new_image.show()
    return inverted_array


def ft_red(array: ndarray) -> ndarray:
    """Keep only the red channel."""
    red_channel = array[:, :, 0]
    image = np.zeros_like(array)
    image[:, :, 0] = red_channel
    new_image = Image.fromarray(image)
    new_image.save("red.jpg")
    new_image.show()
    return image


def ft_green(array: ndarray) -> ndarray:
    """
        Keep only the green channel.
    """
    green_channel = array[:, :, 1]
    image = np.zeros_like(array)
    image[:, :, 1] = green_channel
    new_image = Image.fromarray(image)
    new_image.save("green.jpg")
    new_image.show()
    return image


def ft_blue(array: ndarray) -> ndarray:
    """Keep only the blue channel."""
    blue_channel = array[:, :, 2]
    image = np.zeros_like(array)
    image[:, :, 2] = blue_channel
    new_image = Image.fromarray(image)
    new_image.save("blue.jpg")
    new_image.show()
    return image


def ft_grey(array: ndarray) -> ndarray:
    """Convert RGB image to grayscale using average (division only)."""
    # Sum the RGB channels, then divide by 3
    grey = (array[:, :, 0] / 3 + array[:, :, 1] / 3 + array[:, :, 2] / 3).astype(np.uint8)
    grey_3channel = np.stack((grey, grey, grey), axis=-1)
    new_image = Image.fromarray(grey_3channel)
    new_image.save("grey.jpg")
    new_image.show()
    return grey_3channel
