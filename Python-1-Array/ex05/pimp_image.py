
import numpy as np
from numpy import ndarray
from PIL import Image

def ft_invert(array: ndarray) -> ndarray:
   """ invert """
   array = 255 - array
   print(f"New shape after Inverts : {array.shape}")
   #  print(array)


   new_image = Image.fromarray(array)
   new_image.save("invert.jpg")
    
   new_image.show()
   return array

def ft_red(array: ndarray) -> ndarray:
   """ """
   red_channel = array[:, :, 0]
   image = np.zeros_like(array)

   image[:, :, 0] = red_channel

   new_image = Image.fromarray(image)
   new_image.save("red.jpg")

   new_image.show()
   return image


def ft_green(array: ndarray) -> ndarray:
   """ """
   green_channel = array[:, :, 1]
   image = np.zeros_like(array)

   image[:, :, 1] = green_channel

   new_image = Image.fromarray(image)
   new_image.save("green.jpg")
   
   new_image.show()

   return image

def ft_blue(array: ndarray) -> ndarray:
   """ """
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