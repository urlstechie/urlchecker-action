#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
from core.fileproc import collect_links_from_file
from core.urlproc import check_response_status_code, check_urls


@pytest.mark.parametrize('file', ["tests/test_files/sample_test_file.md",
                                  "tests/test_files/sample_test_file.py"])
def test_check_urls(file):
    """
    test check urls check function.
    """
    urls = collect_links_from_file(file)
    check_urls(file, urls, check_results=[[],[]])
