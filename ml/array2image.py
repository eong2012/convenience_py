from matplotlib import pyplot as plt
import numpy as np

__author__ = 'ronny'


# ==============================================================================
#                                                                    ARRAY2IMAGE
# ==============================================================================
def array2image(x, reshape=None, cmap="gray", colorbar=False, smooth=False,
                save=None, show=True):
    """
    Takes a 2D array and converts it to an image.

    :param x: {numpy array}
        The array to create an image from
    :param reshape: {tuple of two integers} (default=None)
        If the array `x` is not already a 2D array, then specify the desired
        dimensions (num_rows, num_cols).
    :param cmap: {string} (default="gray")
        Colormap to use. This value is passed on to  matplotlib.pyplot.imshow()
        So whatever values are valid for that function can be used here.
        Some possible values:
            "gray"     = grayscale (default)
            "spectral" = reverse rainbow heatmap from black to VIBGYOR to white
            "hot"      = heatmap (black, red, yellow, white)
    :param colorbar: {boolean}(default=False)
        Should it display a colorbar to interpret values of the image colors?

    :param smooth: {boolean} (default = False)
        If set to False (default), then it draws square pixels of a solid color
        determined by the corresponding value in the array.

        If set to True, then it performs a gradient interpolation between
        neighboring points. The result is a smoother (if blurier) image.

    :param save: {None or string} (default=None)
        Allows you to save the image to a file by specifying a filepath/filename
    :param show: {boolean} (default=True)
        Show the image in a window?
    """
    # ==========================================================================
    # Reshape to a 2D array
    if reshape is not None:
        if isinstance(reshape, tuple) and len(reshape) == 2:
            x = np.array(x).reshape(reshape)
        else:
            msg = "`reshape` argument should the a tuple of two integers"
            raise ValueError(msg)

    # Set interpolation method based on smooth argument
    interpolation = "bicubic" if smooth else "nearest"

    # Create image
    plt.figure()
    plt.imshow(x, cmap=cmap, interpolation=interpolation)

    # Show a colorbar if it was asked for.
    if colorbar:
        plt.colorbar()

    # Save the image if requested
    if save is not None:
        plt.savefig(save)

    # show image if it is requested
    if show:
        plt.show()


