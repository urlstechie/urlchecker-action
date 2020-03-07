#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests
from core import urlmarker


def check_response_status_code(url, response, print_format):
    """
    check and print response status of an input url.

    Args:
        url          (str) : url text.
        response    (list) : request response from the url request.
        print_format (str) : format to print the logs according to.
    """
    if response.status_code == 200:
        print(print_format % (url, "\x1b[31m" + "." + "\x1b[0m"))
    else:
        print(print_format % (url, "\x1b[32m" +"x" + "\x1b[0m"))


def check_urls(file, urls):
    """
    check urls extracted from a certain file and print the checks results.

    Args:
        file  (str) : path to file.
        urls (list) : list of urls to check.
    """
    # get longest url size
    long_url = str(max([len(url) for url in urls]))

    # define orint format
    print_format = "%" + long_url + "s %10s"

    # chech links
    for url in [url for url in urls if "http" in url]:
        url_termination = "." + os.path.basename(url).split(".")[-1]

        try:
            response = requests.get(
                url, stream=True, allow_redirects=True, timeout=5)
            check_response_status_code(url, response, print_format)

        except requests.exceptions.Timeout as e:
            print(e)

        except requests.exceptions.ConnectionError:
            print(print_format % (url, "\x1b[32m" +"x" + "\x1b[0m"))

        except Exception as e:
            print(e.message)
