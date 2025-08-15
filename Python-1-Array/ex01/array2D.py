# REF : https://courses.lumenlearning.com/calculus2/chapter/volume-and-the-slicing-method/
import numpy


def slice_me(family: list, start: int, end: int) -> list:
    """
        Slices a 2D list (matrix) from row index `start` to `end` (exclusive)
        and prints the original and new shapes.

        Args:
            family (list): A 2D list (list of lists).
            start (int): Start row index.
            end (int): End row index (exclusive).

        Returns:
            list: The sliced 2D list.
    """
    try:
        assert isinstance(family, list), "family must be a list"
        assert all(isinstance(row, list) for row in family), "All elements of family must be lists"
        assert all(len(row) == len(family[0]) for row in family), "All rows must have the same number of columns"
        # row = len(family)
        # colum = len(family[0])
        # print(f"My shape is : ({row}, {colum})")
        # for r in family:
        #     if len(r) != colum:
        #        raise ValueError("All rows must have the same number of columns")
        # sliced = family[start:end]
        # print(f"My new shape is : ({len(sliced)}, {colum})")
        # return sliced
        # After Discover Numpy Magic
        # print(f"Type(family): {type(family)}")
        ndarray = numpy.array(family)
        print(f"My shape is : {ndarray.shape}")
        print(f"My new shape is : {ndarray[start:end].shape}")
        return ndarray[start:end]
    except Exception as error:
        print(f"Error: {error}")
