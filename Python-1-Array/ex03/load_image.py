import numpy as np
from numpy import ndarray
from PIL import Image

def ft_load(path: str) -> ndarray:
    try:
        with Image.open(path) as image:
            imageNp = np.asarray(image)
            print(f"The shape of image is : {imageNp.shape}")
            print(imageNp)
            return imageNp


    except Exception as e:
        print(e)