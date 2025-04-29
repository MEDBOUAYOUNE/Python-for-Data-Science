
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

# def ft_red(array) -> array:
#    """ """

# def ft_green(array) -> array:
#    """ """

# def ft_blue(array) -> array:
#    """ """

# def ft_grey(array) -> array:
#     """ """