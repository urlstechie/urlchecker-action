#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests
from core import urlmarker
from termcolor import colored


def check_response_status_code(url, response, print_format):
    """
    check and print response status of an input url.

    Args:
        url          (str) : url text.
        response    (list) : request response from the url request.
        print_format (str) : format to print the logs according to.
    """
    if response.status_code == 200:
        print(print_format % (url, colored(".", "green")))
        return f"{url} ✓"
    else:
        print(print_format % (url, colored("x", "red")))
        return f"{url} ✘"


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
    results = []
    for url in [url for url in urls if "http" in url]:
        url_termination = "." + os.path.basename(url).split(".")[-1]

        try:
            response = requests.get(
                url, stream=True, allow_redirects=True, timeout=5)
            result = check_response_status_code(url, response, print_format)
            results.append(result)

        except requests.exceptions.Timeout as e:
            print(e)

        except requests.exceptions.ConnectionError:
            print(print_format % (url, colored("x", "red")))
            results.append(f"{url} ✘")

        except Exception as e:
            print(e.message)

    return "\n".join(results)
