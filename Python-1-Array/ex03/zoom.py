from load_image import ft_load
from PIL import Image


def zoom(path: str) -> None:
    """
    Zooms into a specific region of an image and saves the cropped image.
    Args:
        path (str): The file path to the image.
        Returns:
        None
        Raises:
            FileNotFoundError: If the image file does not exist.
            ValueError: If the image cannot be opened or converted.
    """
    _ndarray = ft_load(path)
    print(_ndarray)
    _ndarray = _ndarray[150:550, 400:800, 1]
    print(f"New shape after slicing: {_ndarray.shape}")
    print(_ndarray)
    new_image = Image.fromarray(_ndarray)
    new_image.save("cropped_image.jpg")
    new_image.show()


def main():
    """ """
    try:
        zoom("animal.jpeg")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
