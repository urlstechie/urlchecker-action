#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pytest
from core.fileproc import check_file_type, get_file_paths, collect_links_from_file, include_file


@pytest.mark.parametrize('file_path', ["tests/test_files/sample_test_file.md",
                                       "tests/test_files/sample_test_file.py"])
@pytest.mark.parametrize('file_types', [[".md", ".py"]])
def test_check_file_type(file_path, file_types):
    """
    test check file types
    """
    output = check_file_type(file_path, file_types)
    if not output:
        raise AssertionError

    # check for false
    output = check_file_type(file_path + ".nonesense", file_types)
    if output:
        raise AssertionError


@pytest.mark.parametrize('file_path', ["tests/test_files/sample_test_file.md",
                                       "tests/test_files/sample_test_file.py"])
@pytest.mark.parametrize('white_list_patterns', [["[.py]"], ["[.md]"], ["tests/test_file"]])
def test_include_files(file_path, white_list_patterns):
    """
    test if a file should be included based on patterns (using extension for test)
    """
    _, extension = os.path.splitext(file_path)
    expected = not extension in file_path
    result = include_file(file_path, white_list_patterns)

    # No files should be included for a global path pattern
    if "tests/test_file" in white_list_patterns:
        if result:
            raise AssertionError

    # Otherwise, the patterns should honor extension
    else:
        if result != expected:
            raise AssertionError

@pytest.mark.parametrize('base_path', ["tests/test_files"])
@pytest.mark.parametrize('file_types', [[".md", ".py"]])
def test_get_file_paths(base_path, file_types):
    """
    get path to all files under a give directory and its subfolders.

    Args:
        base_path   (str) : base path.
        file_types (list) : list of file extensions to accept.

    Returns:
        list of file paths.
    """
    file_paths = get_file_paths(base_path, file_types)
    expected_paths = [["tests/test_files/sample_test_file.md",
                       "tests/test_files/sample_test_file.py"],
                     ["tests/test_files/sample_test_file.py",
                      "tests/test_files/sample_test_file.md"]]
    # assert
    assert(file_paths in expected_paths)


@pytest.mark.parametrize('file_path', ["tests/test_files/sample_test_file.md",
                                       "tests/test_files/sample_test_file.md"])
def collect_links_from_file(file_path):
    """
    test links collerction function.
    """
    # read file content
    urls = collect_links_from_file()
    assert(len(url) == 3)
