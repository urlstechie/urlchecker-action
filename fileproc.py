import re
import os
import urlmarker
import urllib.request
from termcolor import colored


def check_file_type(file, file_types):
    """
    check file type to assert that only file with certain predefined extensions
    are checked.

    Args:
        file        (str) : file name.
        file_types (list) : list of file extensions to accept.
    """
    ftype = "." + file.split(".")[-1]
    if ftype in file_types:
        return True
    else:
        return False


def get_file_paths(path, file_types=[".py", ".md", ".c", ".rst"]):
    """
    get path to all files under a give directory and its subfolders.

    Args:
        path (string) : base path.

    Returns:
        list of file paths.
    """
    # init paths
    file_paths = []

    # r = root, d = directories, f = files
    for root, directory, files in os.walk(path):
        file_paths += [
            os.path.join(root, file) for file in files
            if os.path.isfile(os.path.join(root, file))
            and check_file_type(file, file_types)
        ]
    return file_paths


def collect_links_from_file(file_path):
    """
    collect all links in a file.
    """
    # read file content
    with open(file_path, 'r') as file:
        content = file.read()

    # get and filter urls
    urls = re.findall(urlmarker.URL_REGEX, content)
    urls = [url for url in urls if "http" in url]
    return urls
