from os import path


def viewFile(_path: str, _file: str) -> str:
    """Returns the contents of a json file

    Args:
        _path (str): Path to the file
        _file (str): Name of the file

    Returns:
        str: Contents of the json file
    """
    with open(path.join(_path, _file)) as fp:
        return fp.read()
