from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Load image from path, prins its format and its pixels
    content in RGB format
    """
    try:
        # load the image
        image = Image.open(path)
        # convert PIL images into NumPy arrays
        numpydata = np.asarray(image)
        # shape output denotes (height, width, no.of color channels)
        print("The shape of image is:", numpydata.shape)
        print(numpydata)
        return (numpydata)
    except Exception as e:
        print(type(e).__name__ + ":", e)
        exit(1)