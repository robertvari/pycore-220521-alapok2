import os


def get_all_files(root_folder: str, file_list: list):
    # doc string
    """
    Recursive lists all files in a folder and subfolders.
    :param root_folder: The root folder (str)
    :param file_list: An empty list to store result
    :return: None
    """

    folder_content = [os.path.join(root_folder, i) for i in os.listdir(root_folder)]