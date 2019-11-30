#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
from check import clone_rep, del_repo, check_repo


@pytest.mark.parametrize('git_path', ["https://github.com/SuperKogito/SuperKogito.github.io"])
def test_clone_repo(git_path):
    """
    test clone repo function.
    """
    cloning_status = clone_rep(git_path)
    assert(cloning_status == True)


@pytest.mark.parametrize('base_path', ["SuperKogito.github.io"])
def test_del_repo(base_path):
    """
    test del repo function.
    """
    deletion_status = del_repo(base_path)
    assert(deletion_status == True)


@pytest.mark.parametrize('file_paths', [["tests/test_files/sample_test_file.md"],
                                        ["tests/test_files/sample_test_file.py"]])
@pytest.mark.parametrize('print_all', [False, True])
def test_check_repo(file_paths, print_all):
    """
    test check repo function.
    """
    check_repo(file_paths, print_all)
