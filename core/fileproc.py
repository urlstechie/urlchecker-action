#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os
from core import urlmarker


def check_file_type(file_path, file_types):
    """
    Check file type to assert that only file with certain predefined extensions
    are checked.

    Args:
        - file_path   (str) : path to file.
        - file_types (list) : list of file extensions to accept.

    Returns:
        (bool) true if file type is supported else false.
    """
    ftype = "." + file_path.split(".")[-1]
    if ftype in file_types:
        return True

    # default return
    return False


def include_file(file_path, white_list_patterns):
    """
    Check a file path for inclusion based on an OR regular expression.
    The user is currently not notified if a file is marked for removal.

    Args:
        - file_path            (str) : a file path to check if should be included.
        - white_list_patterns (list) : list of patterns to whitelist (include).

    Returns:
        (bool) boolean indicating if the URL should be white listed (included).
    """
    # No white listed patterns, all files are included
    if not white_list_patterns:
        return True

    # Return False (don't include) if the patterns match
    regexp = "(%s)" % "|".join(white_list_patterns)
    return not re.search(regexp, file_path)


def get_file_paths(base_path,
                   file_types,
                   white_listed_files=None):
    """
    Get path to all files under a give directory and its subfolders.

    Args:
        - base_path           (str) : base path.
        - file_types         (list) : list of file extensions to accept.
        - white_listed_files (list) : list of files or patterns to white list

    Returns:
        (list) list of file paths.
    """
    white_listed_files = white_listed_files or []

    # init paths
    file_paths = []

    # walk folders and colect file paths
    for root, directory, files in os.walk(base_path):
        file_paths += [
                        os.path.join(root, file) for file in files
                        if os.path.isfile(os.path.join(root, file))
                        and check_file_type(file, file_types)
                        and include_file(os.path.join(root, file), white_listed_files)
                      ]
    return file_paths


def collect_links_from_file(file_path, unique=True):
    """
    Collect all links in a file.

    Args:
        - file_path   (str) : path to file.

    Returns:
        (list) list of links/ urls in a file.
    """
    # read file content
    with open(file_path, 'r') as file:
        content = file.read()

    # get and filter urls
    urls = re.findall(urlmarker.URL_REGEX, content)
    urls = [url.strip() for url in urls if url.strip().startswith('http')]
    urls = [url.strip('\\n') if url.endswith('\\n') else url for url in urls]

    # Do we only want unique links?
    if unique:
        return list(set(urls))

    return urls
