import os
import requests
import urlmarker
from termcolor import colored


def check_response_status_code(url, response, print_format):
    if response.status_code == 200:
        print(print_format % (url, colored(".", "green")))
    else:
        print(print_format % (url, colored("x", "red")))


def retrieve_response(url, signum, frame):
    response = requests.get(url)
    return response


def check_urls(file, urls):
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
            print(print_format % (url, colored("x", "red")))
