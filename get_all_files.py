import glob

def get_all_files(root, filetype=None):
    '''
    Parameters
    ----------
    root : str
        filepath root
    filetype : str
        Optional filter by filetype. Returns all files otherwise.

    Returns
    -------
    list of files with directory

    Example
    -------
    file_list = []
    glob_files('/FEStrategy/Hanweck_HDF5')
    print(file_list[0:2])

    ['/FEStrategy/Hanweck_HDF5/2017/12/07/AMZN.h5', '/FEStrategy/Hanweck_HDF5/2017/12/07/FB.h5']
    '''
    glob_files(root)

    if filetype is not None:
        file_list = [f for f in file_list if filetype in f]

    return file_list

def glob_files(root):
    '''
    Parameters
    ----------
    root : str
        root file path

    Returns
    -------
    Nothing but has global variable file_list

    Example
    -------
    glob_files('/FEStrategy/')
    '''
    global file_list
    files = glob.glob(root + '*')

    if files == []:

        try:
            file_list += [root[:-1]]
        except:
            file_list = [root[:-1]]

    else:
        for f in files:
            glob_files(f + '/')
