from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_transpose_3D(array: np.ndarray):
    """
    Transposes a 3D matrix
    """
    x, y, z = array.shape
    new_array = np.zeros((y, x, z), dtype=np.int32)
    for i in range(x):
        for j in range(y):
            for k in range(z):
                new_array[i][j][k] = array[j][i][k]
    return (new_array)


# def ft_transpose(array: np.ndarray):
#     """
#     Transposes a 2D matrix
#     """
#     x,y = array.shape
#     new_array = np.zeros((y, x), dtype=np.int32)
#     for i in range(x):
#         for j in range(y):
#             new_array[j][i] = array[i][j]
#     return(new_array)

def rotate(array: np.ndarray):
    """
    Rotates the image array  usinf ft_transpose function
    and displays it using matplotlib
    """
    try:
        # extract the red, green, and blue channels
        # resulting array shape is (height, width, 1)
        red_channel = array[:, :, 0:1]
        green_channel = array[:, :, 1:2]
        blue_channel = array[:, :, 2:3]

        # #transpose the red, green, and blue channels
        red_transpose = ft_transpose_3D(red_channel)
        green_transpose = ft_transpose_3D(green_channel)
        blue_transpose = ft_transpose_3D(blue_channel)

        # concatenate the red, green, and blue channels ALONG the third axis
        rgb_array = np.concatenate(
            (red_transpose, green_transpose, blue_transpose), axis=2)

        sliced_arr = rgb_array[:, :, 0]
        print("New shape after Transpose: {}".format(sliced_arr.shape))
        print(sliced_arr)

        # Display slice of transposed image
        fig, ax = plt.subplots()
        ax.imshow(sliced_arr, cmap='gray')
        plt.show()

    except Exception as e:
        print(type(e).__name__ + ":", e)
        exit(1)
    except KeyboardInterrupt:
        exit(1)


def ft_crop(array: np.ndarray):
    """
    Crops the image base on (x1,y1) and (x2,y2) values
    """
    # Adjust these values based on your desired region to be zoomed
    x1, y1, x2, y2 = 450, 100, 850, 500
    # (x1,y1) is the top left corner and (x2,y2) is the bottom right corner
    return array[y1:y2, x1:x2]


def ft_slice(array: np.ndarray):
    """
    Slices the image array to to remove any color channel
    and prints its shape and content
    """
    sliced_arr = array[:, :, 0:1]
    print("The shape of image is: {}" .format(sliced_arr.shape))
    print(sliced_arr)


def main():
    try:
        image_arr = ft_load("../animal.jpeg")
        cropped_arr = ft_crop(image_arr)
        ft_slice(cropped_arr)
        print("----------------------------------------")
        rotate(cropped_arr)
    except Exception as e:
        print(type(e).__name__+":", e)
        exit(1)


if __name__ == "__main__":
    main()

"""
#References: Transpose of a 3D matrix
https://www.youtube.com/watch?v=ydosxH65pdA
https://www.youtube.com/watch?v=K81AdVw3BkA
"""
