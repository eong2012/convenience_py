from os.path import exists as file_exists
from pickle import load as pickle_load
from pickle import dump as pickle_dump

# ==============================================================================
#                                                             CACHE CALCULATIONS
# ==============================================================================
def cache_calc(filename, func, *args, **kwargs):
    """ Cache calculations, so that the first call to this function performs the
        calculations, and caches them to a file. Future calls to this function
        simply load up the data from the cached file.

    Args:
        filename:(str)
            the file path you want to save the cached file as
        func: (callable)
            The function to call to calculate the
        *args:
            ordered arguments to be passed on to func()
        **kwargs:
            keyword arguments to be passed on to func()

    Returns:
        Returns whatever func() returns.
    
    Examples:
        cache_calc("myCachedFile", myFunc)
    """
    # ==========================================================================
    if file_exists(filename):
        print("Loading the cached version of " + filename)
        with open(filename, mode="rb") as fileObj:
            x = pickle_load(fileObj)
    else:
        print("Caching the calculation to the file " + filename)
        x = func(*args, **kwargs)
        # Cache the calculation so future calls to this function load the cached
        # object instead.
        with open(filename, mode="wb") as fileObj:
            pickle_dump(x, fileObj)
    return x


