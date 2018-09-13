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
    get_all_files('/')

    '''
    global file_list
    file_list = []
    _glob_files(root)

    if filetype is not None:
        file_list = [f for f in file_list if filetype in f]

    return list(set(file_list))

def _glob_files(root):
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
    _glob_files('/')
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
            _glob_files(f + '/')
