#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random
import requests
import time
from core import urlmarker


def record_response(url, response, check_results):
    """
    record response status of an input url. This function is run after success,
    or at the end of retry to record the final response.

    Args:
        url          (str) : url text.
        response    (list) : request response from the url request.
        check_results (list) : list of lists, success appended to 0, failure to 1.
    """
    # response of None indicates a failure
    if not response:
        check_results[1].append(url)

    # success
    elif response.status_code == 200:
        check_results[0].append(url)

    # Any other error
    else:
        check_results[1].append(url)

    return check_results

def check_response_status_code(url, response):
    """
    check response status of an input url. Returns a boolean
    to indicate if retry is needed.

    Args:
        url          (str) : url text.
        response    (list) : request response from the url request.
    """
    # Case 1: response is None indicating triggered error
    if not response:
        print("\x1b[31m" + url + "\x1b[0m")
        return True

    # Case 2: succcess!
    if response.status_code == 200:
        print("\x1b[32m" + url + "\x1b[0m")
        return False

    # Case 3: failure of some kind
    print("\x1b[31m" + url + "\x1b[0m")
    return True


def get_user_agent():
    """Return a randomly chosen user agent for requests
    """
    agents = [
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/57.0.2987.110 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/61.0.3163.79 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
         'Gecko/20100101 '
         'Firefox/55.0'),  # firefox
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/61.0.3163.91 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/62.0.3202.89 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/63.0.3239.108 '
         'Safari/537.36'),  # chrome
    ]
    return random.choice(agents)


def check_urls(file, urls, retry_count=1, timeout=5):
    """
    check urls extracted from a certain file and print the checks results.

    Args:
        file  (str) : path to file.
        urls (list) : list of urls to check.
        retry_count (int): a number of retries to issue (defaults to 1, no retry)
    """
    # init results list (first is success, second is issue)
    check_results = [[], []]
    seen = set()

    # we will double the time for retry each time
    retry_seconds = 2

    # Some sites will return 403 if it's not a "human" user agent
    user_agent = get_user_agent()
    headers = {'User-Agent': user_agent}

    # check links
    for url in [url for url in urls if "http" in url]:

        # init do retrails and retrails counts
        do_retry = True
        rcount = retry_count

        # With retry, increase timeout by a second
        pause = timeout

        # get url termination
        url_termination = "." + os.path.basename(url).split(".")[-1]

        # No need to test the same URL twice
        if url in seen:
            continue

        seen.add(url)
        while rcount > 0 and do_retry:
            response = None
            try:
                response = requests.get(url, timeout=pause, headers=headers)

            except requests.exceptions.Timeout as e:
                print(e)

            except requests.exceptions.ConnectionError:
                continue

            except Exception as e:
                print(e.message)

            # decrement retrials count
            rcount-=1

            # Break from the loop if we have success, update user
            do_retry = check_response_status_code(url, response)

            # If we try again, pause for retry seconds and update retry seconds
            if do_retry:
                print("Retry %s for %s, timeout %s" %(rcount, url, pause))
                time.sleep(retry_seconds)
                retry_seconds = retry_seconds * 2
                pause += 1

        # When we break from while, we record final response
        check_results = record_response(url, response, check_results)

    return check_results
