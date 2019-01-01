"""
file_iterator.py : Utility for iterating in directory and get the files in it.

"""

import os

def get_files_from_directory(dirname, exclude_dirs = []):
    '''
    This function will walk throughout the directory and returns the files
    params: dirname, exlude_dirs

    The exclude dir is the list of folders which you want to skip while iterating

    '''
    assert os.path.exists(dirname), "The given directory %s is not exists"%dirname

    for root, dirs, files in os.walk(dirname):
        for exdir in exclude_dirs:
            if exdir in dirs:
                dirs.remove(exdir)
        for filename in files:
            yield os.path.join(root, filename)


#usage
for filename in get_files_from_directory(r"e:\study", ['test']):
    print filename


