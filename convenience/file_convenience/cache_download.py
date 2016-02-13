from __future__ import print_function
import os
from urllib import urlretrieve


#===============================================================================
#                                                                 CACHE_DOWNLOAD
#===============================================================================
def cache_download(url, out=("", "")):
    """
    Downloads a file if it is not already downloaded in the output path.

    :param url: {string}
        url of the file to download
    :param out: {tuple of 2 Strings}
        Tuple with two string elements:

        1. The first element is the directory you want to save the  file to.
           if this is an empty string "", then it will save it automatically to
           the current working directory.
        2. The second element is the filename you want to save it as. If this is
           an empty string "", then it automatically saves it as the same
           as the remote file being downloaded.

        Default is ("", "") which saves the file in the current working
        directory without changing the filename.
    """
    # ==========================================================================
    #---------------------------------------------------------------------------
    #                                                     Extract local filepath
    # --------------------------------------------------------------------------
    check that out is a tuple with 2 string elements
    if not (isinstance(out, (tuple, list))
            and isinstance(out[0], str)
            and isinstance(out[1], str)):
        raise ValueError("out argument should be a tuple of 2 strings")

    # Use same filename as remote file if no local one specified.
    if out[1] == "":
        out = list(out)
        out[1] = os.path.basename(url)

    out_file = os.path.join(*out)

    # print("Output file:"+out_file)
    # print("downloaing from:", url)
    # --------------------------------------------------------------------------
    #                                                 Check if local file exists
    # --------------------------------------------------------------------------
    if os.path.exists(out_file):
        #TODO: check the local file is the correct file.

        # No need to download file again, so terminate here.
        print("File already exists, keeping cached copy")
        return None

    # --------------------------------------------------------------------------
    #                                                              Download File
    # --------------------------------------------------------------------------
    try:
        urlretrieve(url, out_file)
    except:
        raise Exception('failed to download from' + url)

