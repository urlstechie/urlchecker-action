#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from core import urlproc
from core import fileproc


def clone_repo(git_path, branch="master"):
    """
    Clone and name a git repository.

    Args:
        - git_path (str) : https path to git repository.
        - branch   (str) : name of the brankch to use. Default="master"

    Returns:
        (str) base path of the cloned git repository.
    """
    base_path = os.path.basename(git_path)
    result = subprocess.run(["git", "clone", "-b", branch, git_path, base_path],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    if result.returncode != 0:
        sys.exit("Issue with cloning branch %s of %s" % (branch, git_path))

    return base_path


def del_repo(base_path):
    """
    Delete repository.

    Args:
        - base_path (str) : base path of the cloned git repository.

    Returns:
        (str) message/ code describing whether the operation was successfully excuted.
    """
    # clone repo
    result = subprocess.run(["rm", "-R", "-f", base_path],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    return result.returncode


def white_listed(url, white_listed_urls, white_listed_patterns):
    """
    Check if link is in the white listed URLs or patterns to ignore.

    Args:
        - url                    (str) : link to check.
        - white_listed_urls     (list) : list of white-listed urls.
        - white_listed_patterns (list) : list of white-listed patterns.

    Returns:
        (bool) boolean for whether link is white-listed or not.
    """
    # check white listed urls
    if url in white_listed_urls:
        return True

    # check white listed patterns
    i = 0
    while i < len(white_listed_patterns):
        if white_listed_patterns[i] in url:
            return True
        i += 1

    # default return
    return False


def check_repo(file_paths,
               print_all,
               white_listed_urls,
               white_listed_patterns,
               retry_count=1,
               timeout=5):
    """
    Check all urls extracted from all files in a repository.

    Args:
        - file_paths            (list) : list of file paths with urls to check.
        - print_all              (str) : control var for whether to print all checked file names or only the ones with urls.
        - white_listed_urls     (list) : list of white-listed urls.
        - white_listed_patterns (list) : list of white-listed patterns.
        - retry_count            (int) : number of retries on failed first check. Default=1.
        - timeout                (int) : timeout to use when waiting on check feedback. Default=5.

    Returns:
        (list) check-results as a list of two lists (successfull checks, failed checks).
    """
    # init results list (first is success, second is issue)
    check_results = [[], []]

    # loop files
    for file in file_paths:

        # collect links from each file (unique=True is set)
        urls = fileproc.collect_links_from_file(file)

        # eliminate white listed urls and white listed white listed patterns
        if white_listed_urls or white_listed_patterns:
            urls = [url for url in urls
                    if not white_listed(url,
                                        white_listed_urls,
                                        white_listed_patterns)]

        # if some links are found, check them
        if urls:
            print("\n", file, "\n", "-" * len(file))
            urlproc.check_urls(file, urls, check_results, retry_count, timeout)

        # if no urls are found, mention it if required
        else:
            if print_all == "true":
                print("\n", file, "\n", "-" * len(file))
                print("No urls found.")

    return check_results


def get_branch():
    """
    Derive the selected branch. We first look to the environment variable
    for INPUT_BRANCH, meaning that the user set the branch variable. If
    that is unset we parse GITHUB_REF. If both of those are unset,
    then we default to master.

    Returns:
        (str) the branch found in the environment, otherwise master.
    """
    # First check goes to use setting in action
    branch = os.getenv("INPUT_BRANCH")
    if branch:
        return branch

    # Second check is for GITHUB_REF
    branch = os.getenv("GITHUB_REF")
    if branch:
        branch = branch.replace("refs/heads/", "")
        return branch
    return "master"


if __name__ == "__main__":

    # read input variables
    git_path = os.getenv("INPUT_GIT_PATH", "")
    branch = get_branch()
    subfolder = os.getenv("INPUT_SUBFOLDER", "")
    cleanup = os.getenv("INPUT_CLEANUP", "false").lower()
    file_types = os.getenv("INPUT_FILE_TYPES", "").split(",")
    print_all = os.getenv("INPUT_PRINT_ALL", "").lower()
    white_listed_urls = urlproc.remove_empty(os.getenv("INPUT_WHITE_LISTED_URLS", "").split(","))
    white_listed_patterns = urlproc.remove_empty(os.getenv("INPUT_WHITE_LISTED_PATTERNS", "").split(","))
    white_listed_files = urlproc.remove_empty(os.getenv("INPUT_WHITE_LISTED_FILES", "").split(","))
    force_pass = os.getenv("INPUT_FORCE_PASS", "false").lower()
    retry_count = int(os.getenv("INPUT_RETRY_COUNT", 1))
    timeout = int(os.getenv("INPUT_TIMEOUT", 5)) # seconds

    # clone project repo if defined
    base_path = os.environ.get("GITHUB_WORKSPACE", os.getcwd())

    # Alert user about settings
    print("      base path: %s" % base_path)
    print("       git path: %s" % git_path)
    print("      subfolder: %s" % subfolder)
    print("         branch: %s" % branch)
    print("        cleanup: %s" % cleanup)
    print("     file types: %s" % file_types)
    print("      print all: %s" % print_all)
    print(" url whitetlist: %s" % white_listed_urls)
    print("   url patterns: %s" % white_listed_patterns)
    print("  file patterns: %s" % white_listed_files)
    print("     force pass: %s" % force_pass)
    print("    retry count: %s" % retry_count)
    print("        timeout: %s" % timeout)

    # If a custom base path is provided, clone and use it
    if git_path not in ["", None]:
        base_path = clone_repo(git_path, branch)

    if subfolder not in ["", None]:
        base_path = os.path.join(base_path, subfolder)

    # Assert that the base path exists
    if not os.path.exists(base_path):
        sys.exit("Cannot find %s to check" % base_path)

    # get all file paths
    file_paths = fileproc.get_file_paths(base_path=base_path,
                                         file_types=file_types,
                                         white_listed_files=white_listed_files)

    # check repo urls
    check_results = check_repo(file_paths=file_paths,
                               print_all=print_all,
                               white_listed_urls=white_listed_urls,
                               white_listed_patterns=white_listed_patterns,
                               retry_count=retry_count,
                               timeout=timeout)

    # delete repo when done, if requested
    if cleanup == "true":
        del_repo(base_path)

    # exit
    if len(check_results) == 0:
        print("\n\nDone. No links were collected.")
        sys.exit(0)

    elif force_pass == "false" and len(check_results[1]) > 0 :
        print("\n\nDone. The following URLS did not pass:")
        for failed_url in check_results[1]:
            print("\x1b[31m" + failed_url + "\x1b[0m")
        sys.exit(1)

    else :
        print("Done. All URLS passed.")
        sys.exit(0)
