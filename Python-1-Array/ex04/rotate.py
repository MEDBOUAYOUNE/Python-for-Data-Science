from load_image  import ft_load
from PIL import Image
from numpy import ndarray

#Source: https://stackoverflow.com/questions/69994725/how-to-reshape-numpy-arrays-to-turn-rows-into-columns

def rotate(path: str)-> None:
    """ """
    _ndarray = ft_load(path)
    _ndarray = _ndarray[150:550, 400:800, 1]
    _ndarray = _ndarray.reshape(400, 400).transpose()
    print(f"New shape after Transpose:: {_ndarray.shape}")
    print(_ndarray)


    new_image = Image.fromarray(_ndarray)
    new_image.save("rotated.jpg")
    
    new_image.show()


if __name__ == "__main__":
    rotate("animal.jpeg")