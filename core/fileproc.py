#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os
from core import urlmarker


def check_file_type(file_path, file_types):
    """
    check file type to assert that only file with certain predefined extensions
    are checked.

    Args:
        file_path   (str) : path to file.
        file_types (list) : list of file extensions to accept.

    Returns:
        boolean, true if file type is supported else false.
    """
    ftype = "." + file_path.split(".")[-1]
    if ftype in file_types:
        return True

    # default return
    return False


def get_file_paths(base_path, file_types):
    """
    get path to all files under a give directory and its subfolders.

    Args:
        base_path   (str) : base path.
        file_types (list) : list of file extensions to accept.

    Returns:
        list of file paths.
    """
    # init paths
    file_paths = []

    # walk folders and colect file paths
    for root, directory, files in os.walk(base_path):
        file_paths += [
                        os.path.join(root, file) for file in files
                        if os.path.isfile(os.path.join(root, file))
                        and check_file_type(file, file_types)
                      ]
    return file_paths


def collect_links_from_file(file_path):
    """
    collect all links in a file.

    Args:
        file_path   (str) : path to file.

    Returns:
        list of links/ urls in a file.
    """
    # read file content
    with open(file_path, 'r') as file:
        content = file.read()

    # get and filter urls
    urls = re.findall(urlmarker.URL_REGEX, content)
    urls = [url for url in urls if "http" in url]
    return urls
