#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pytest
import configparser
from core.fileproc import get_file_paths
from check import clone_repo, del_repo, check_repo


@pytest.mark.parametrize('git_path', ["https://github.com/SuperKogito/SuperKogito.github.io"])
def test_clone_and_del_repo(git_path):
    """
    test clone and del repo function.
    """
    # test correct functioning
    # clone
    base_path = clone_repo(git_path)
    assert(base_path == os.path.basename(git_path))
    # delete
    deletion_status = del_repo(base_path)
    assert(deletion_status == True)


@pytest.mark.parametrize('file_paths', [["tests/test_files/sample_test_file.md"],
                                        ["tests/test_files/sample_test_file.py"],
                                        ["tests/test_files/sample_test_file.rst"]])
@pytest.mark.parametrize('print_all', [False, True])
@pytest.mark.parametrize('white_listed_urls', [["https://github.com/SuperKogito/SuperKogito.github.io"]])
@pytest.mark.parametrize('white_listed_patterns', [[], ["https://github.com/SuperKogito/SuperKogito.github.io"]])
def test_check_repo(file_paths,
                    print_all,
                    white_listed_urls,
                    white_listed_patterns):
    """
    test check repo function.
    """
    check_repo(file_paths, print_all, white_listed_urls, white_listed_patterns)


@pytest.mark.parametrize('config_fname', ['_local_test_config.conf'])
def test_script(config_fname):
    # init config parser
    config = configparser.ConfigParser()
    config.read(config_fname)

    # init env variables
    os.environ["INPUT_GIT_PATH"] = config['DEFAULT']["git_path_test_value"]
    os.environ["INPUT_FILE_TYPES"] = config['DEFAULT']["file_types_test_values"]
    os.environ["INPUT_PRINT_ALL"] = config['DEFAULT']["print_all_test_value"]
    os.environ["INPUT_WHITE_LISTED_URLS"] = config['DEFAULT']["white_listed_test_urls"]
    os.environ["INPUT_WHITE_LISTED_PATTERNS"] =  config['DEFAULT']["white_listed__test_patterns"]
    # excute script
    os.system("python3 check.py")


@pytest.mark.parametrize('local_folder_path', ['./tests/test_files'])
@pytest.mark.parametrize('config_fname', ['./tests/_local_test_config.conf'])
def test_locally(local_folder_path, config_fname):
    # init config parser
    config = configparser.ConfigParser()
    config.read(config_fname)

    # read input variables
    git_path = local_folder_path
    file_types = config['DEFAULT']["file_types_test_values"].split(",")
    print_all = config['DEFAULT']["print_all_test_value"]
    white_listed_urls = config['DEFAULT']["white_listed_test_urls"].split(",")
    white_listed_patterns = config['DEFAULT']["white_listed__test_patterns"].split(",")

    # debug prints
    print(" config")
    print(" -------")
    print("%25s : %10s" % ("git_path", git_path))
    print("%25s : %10s" % ("file_types", file_types))
    print("%25s : %10s" % ("white_listed_urls", white_listed_urls))
    print("%25s : %10s" % ("white_listed_patterns", white_listed_patterns))

    # get all file paths
    file_paths = get_file_paths(git_path, file_types)

    # check repo urls
    check_repo(file_paths, print_all, white_listed_urls, white_listed_patterns)
    print("Done.")
