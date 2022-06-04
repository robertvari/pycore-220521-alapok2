import os


def get_all_files(root_folder: str, file_list: list):
    # doc string
    """
    Recursive lists all files in a folder and subfolders.
    :param root_folder: The root folder (str)
    :param file_list: An empty list to store result
    :return: None
    """

    # get all content from root_folder (files, folders)
    folder_content = [os.path.join(root_folder, i) for i in os.listdir(root_folder)]

    # collect files
    for i in folder_content:
        if os.path.isfile(i):
            # todo use some kind of filter (name, extension)?
            file_list.append(i)

    # get subfolders
    subfolders = []
    for i in folder_content:
        if os.path.isdir(i):
            subfolders.append(i)

    for folder in subfolders:
        get_all_files(folder, file_list)