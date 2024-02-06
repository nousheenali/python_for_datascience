from load_image import ft_load
from pimp_image import ft_red, ft_blue, ft_grey, ft_green, ft_invert
import matplotlib.pyplot as plt


def draw_image(array, title):
    fig, ax = plt.subplots(3, 2, figsize=(24, 6))
    k = 1
    for i in range(3):
        for j in range(2):
            if title[i * 2 + j] == "Grey":
                # the colormap (cmap) parameter determines how the
                # pixel values are mapped to colors.
                ax[i, j].imshow(array[i * 2 + j], cmap="gray")
            else:
                ax[i, j].imshow(array[i * 2 + j])
            ax[i, j].axis("off")
            str = k.__str__() + ": " + title[i * 2 + j]
            ax[i, j].set_title(str)
            k += 1
    plt.show()


def main():
    try:
        array = ft_load("../landscape.jpg")
        inv = ft_invert(array)
        red = ft_red(array)
        green = ft_green(array)
        blue = ft_blue(array)
        grey = ft_grey(array)
        print(ft_invert.__doc__)

        titles = [
            "Original",
            "Invert",
            "Red",
            "Green",
            "Blue",
            "Grey",
        ]
        # passing image array and respective titles to draw_image function
        draw_image([array, inv, red, green, blue, grey], titles)

    except Exception as e:
        print(type(e).__name__ + ":", e)
        exit(1)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()
