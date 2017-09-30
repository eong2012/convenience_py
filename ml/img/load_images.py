# ==============================================================================
#                                                            LOAD_IMAGE_AS_ARRAY
# ==============================================================================
# USING SCIPY (with i think PIL on the backend)
import scipy.misc
def load_image_as_array(f, rescale=None):
    """ Given a filepath to an image file, it loads an image as a numpy array.
        Optionally resize the images to [width, height]"""
    img = scipy.misc.imread(f)
    if rescale:
        width, height = rescale
        img = scipy.misc.imresize(img, (height,width))
    return img


# USING OPEN CV
def load_image_as_array(f, rescale=None):
    # TODO: Check the order of the dimensions for resizing in open cv
    img = cv2.imread(f, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert to RGB
    if rescale:
        img = cv2.resize(img, rescale)
    return img


