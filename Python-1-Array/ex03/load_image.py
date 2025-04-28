#REF: https://pillow.readthedocs.io/en/stable/reference/Image.html#functions
import numpy as np
from numpy import ndarray
from PIL import Image

def ft_load(path: str) -> ndarray:
    with Image.open(path) as image:
        imageNp = np.asarray(image)
        print(f"The shape of image is : {imageNp.shape}")
        print(imageNp)
        return imageNp
