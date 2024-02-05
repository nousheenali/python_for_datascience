from numpy import array
import numpy as np


def ft_invert(array) -> array:
    """
    Inverts the image
    """
    # Create a new array with the same shape and all values set to 255
    new_array = np.full(array.shape, 255)
    return new_array - array


def ft_red(array) -> array:
    """
    Changes image filter to red
    """
    red_img = array * [1, 0, 0]
    return red_img


def ft_green(array) -> array:
    """
    Changes image filter to green
    """
    # create a new array with the same shape and set green values to 0
    new_array = array.copy()
    new_array[:, :, 1] = 0
    # subtract the new array from the original array to get green filter
    return array - new_array


def ft_blue(array) -> array:
    """
    Changes image filter to blue
    """
    blue_img = array.copy()
    blue_img[:, :, 0:2] = 0
    return blue_img


def ft_grey(array) -> array:
    """
    Convert the image to grey scale
    """
    # Sum the three channels
    sum_array = array.sum(axis=2)
    # average the three channels
    grey_image = sum_array / 3
    return (grey_image)


"""
References:
https://deepnote.com/@gabriele-tazzari-4ac1/Understanding-image-filters-with-Python-d6d7ff84-29f0-4466-a6f0-c5c3dc05345f
"""
