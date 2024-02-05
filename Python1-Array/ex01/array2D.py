import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Returns a slice of a 2D array.
    Args:
        family (list): A 2D array.
        start (int): The start index.
        end (int): The end index.
    Returns:
        list: A slice of the 2D array.
    """
    try:
        print("My shape is :", np.array(family).shape)
        new = np.array(family)[start:end].tolist()
        print("My new shape is :", np.array(new).shape)
        return new
    except Exception as e:
        print(type(e).__name__ + ":", e)
        exit(1)
