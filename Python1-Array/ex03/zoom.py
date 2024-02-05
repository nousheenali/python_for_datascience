"""
Matplotlib is a comprehensive library for creating static, animated,
and interactive visualizations.
"""

from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom(array: np.ndarray):
    """
    Zooms in a RGB image array and displays it using matplotlib
    arguments: array: RGB image array
    """
    try:
        # Adjust these values based on your desired region to be zoomed
        x1, y1, x2, y2 = 450, 100, 850, 500
        # (x1,y1) is the top left corner and (x2,y2) is the bottom right corner
        zoomed_arr = array[y1:y2, x1:x2]
        # get first color channel (index 0)
        sliced_arr = zoomed_arr[:, :, 0:1]
        print("New shape after slicing: {} ".format(sliced_arr.shape))
        print(sliced_arr)
        fig, ax = plt.subplots()  # Create a figure containing a single axes.
        ax.imshow(sliced_arr, cmap='gray')  # Display the image.
        plt.show()
    except Exception as e:
        print(type(e).__name__ + ":", e)
        exit(1)
    except KeyboardInterrupt:
        print("Exit Program")
        exit(1)


def main():
    """
    Loads an image and calls zoom() function
    """
    try:
        image = ft_load("../animal.jpeg")
        print(image)
        zoom(image)
    except Exception as e:
        print(type(e).__name__+":", e)


if __name__ == "__main__":
    main()

"""
#References:
https://regenerativetoday.com/indexing-and-slicing-of-1d-2d-and-3d-arrays-using-numpy/



In the above code, wthough we are extracing the red values os the image,
the image is still displayed in grayscale because we are using cmap='gray'
in the imshow() function. If we remove the cmap='gray' argument, the image
will be displayed in green color. To get the corresponding red, green and
blue images, we can use the following code where we create an empty 3D NumPy
array (temp) filled with zeros, having the same shape as the original image
and then assign the values of the red, green and blue channels to the
corresponding channels of the temp array. Finally, we can display the
three images.
x1, y1, x2, y2 = 450, 100, 850, 500
zoomed_arr = array[y1:y2, x1:x2]
figure, plots = plt.subplots(ncols=3, nrows=1)
    for i, subplot in zip(range(3), plots):
        temp = np.zeros(zoomed_arr.shape, dtype='uint8')
        temp[:,:,i] = zoomed_arr[:,:,i]
        subplot.imshow(temp)
    plt.show()
"""
