from load_image import ft_load
from PIL import Image
from numpy import ndarray


def zoom(path: str) -> None:
    _ndarray = ft_load(path)
    _ndarray = _ndarray[150:550, 400:800]
    print(f"New shape after slicing: {_ndarray.shape}")
    print(_ndarray)
    
    new_image = Image.fromarray(_ndarray)
    new_image.save("cropped_image.jpg")
    
    new_image.show()


if __name__ == "__main__":
    zoom("animal.jpeg")