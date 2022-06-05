import os

ROOT_PATH = os.path.dirname(__file__).replace("utilities", "")
RESOURCE_PATH = os.path.join(ROOT_PATH, "resources")


def get_resource(file_name: str) -> str:
    """
    Given a resource like: bird_01.png gives back the full path.
    :param file_name: (str)
    :return: Full path to the resource file (str)
    """
    file_path = os.path.join(RESOURCE_PATH, file_name)

    assert os.path.exists(file_path), f"File does not exist: {file_path}"
    return file_path


if __name__ == '__main__':
    # test block runs only when this file was executed!!!
    print(get_resource("death.wav"))