import os


#  ---------------------------------------------------------------
# confirm_dir_exists
#  ---------------------------------------------------------------
def confirm_dir_exists(dir_path):
    """
    Makes sure whether the directory path given exists. If it does not,
    then it creates one and returns the path.
    """

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    return dir_path


#  ---------------------------------------------------------------
# confirm_file_exists
#  ---------------------------------------------------------------
def confirm_file_exists(file_path):
    """
    Makes sure whether the file path given exists. If it does not, then it
    creates one and returns the path.
    """
    
    if not os.path.exists(file_path):
        with open(file_path, "w+") as f:
            f.write('')

    return file_path
