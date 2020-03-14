#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import pytest
import subprocess
import configparser
from core.fileproc import get_file_paths
from check import clone_repo, del_repo, check_repo, get_branch


@pytest.mark.parametrize('git_path', ["https://github.com/SuperKogito/SuperKogito.github.io"])
def test_clone_and_del_repo(git_path):
    """
    test clone and del repo function.
    """
    # del repo if it exisits
    if os.path.exists(os.path.basename(git_path)):
        del_repo(os.path.basename(git_path))

    # clone
    base_path = clone_repo(git_path)
    assert(base_path == os.path.basename(git_path))

    # delete should have return code of 0 (success)
    if not del_repo(base_path) == 0:
        raise AssertionError


def test_get_branch():
    """
    test getting branch from environment or default
    """
    # Unset defaults to master
    branch = get_branch()
    if branch != "master":
        raise AssertionError

    # Set both GitHub input variable and ref (ref takes priority)
    for pair in [["INPUT_BRANCH", "devel"], ["GITHUB_REF", "refs/heads/branchy"]]:
        os.environ[pair[0]] = pair[1]
        os.putenv(pair[0], pair[1])

    # Second preference should be for INPUT_BRANCH
    branch = get_branch()
    if branch != "devel":
        raise AssertionError

    del os.environ['INPUT_BRANCH']
    os.unsetenv("INPUT_BRANCH")
    branch = get_branch()
    if branch != "branchy":
        raise AssertionError


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


@pytest.mark.parametrize('config_fname', ['./tests/_local_test_config.conf'])
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
    pipe = subprocess.run(["python3", "check.py"],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)


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


@pytest.mark.parametrize('retry_count', [1, 3])
def test_check_generally(retry_count):
    # init vars
    git_path = "https://github.com/SuperKogito/SuperKogito.github.io.git"
    file_types = [".py", ".md"]
    print_all = "True"
    white_listed_urls = ["https://superkogito.github.io/figures/fig2.html",
                         "https://superkogito.github.io/figures/fig4.html"]
    white_listed_patterns = ["https://superkogito.github.io/tables"]
    timeout = 1
    force_pass = "false"

    # del repo if it exisits
    if os.path.exists(os.path.basename(git_path)):
        del_repo(os.path.basename(git_path))

    # clone repo
    base_path = clone_repo(git_path)

    # get all file paths
    file_paths = get_file_paths(base_path, file_types)

    # check repo urls
    check_results = check_repo(file_paths, print_all, white_listed_urls,
                               white_listed_patterns, retry_count, timeout)

    # exit
    if len(check_results) == 0:
        print("Done. No links were collected.")
        sys.exit(0)

    elif force_pass == "false" and len(check_results[1]) > 0 :
        print("Done. The following URLS did not pass:")
        print("\x1b[31m" + "\n".join(check_results[1]) + "\x1b[0m")
        if retry_count == 1:
            return True

    else :
        print("Done. All URLS passed.")
        if retry_count == 3:
            return True
