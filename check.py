#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from core import urlproc
from core import fileproc


def clone_repo(git_path, branch="master"):
    """
    clone and name a git repository.
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
    delete repository.
    """
    # clone repo
    result = subprocess.run(["rm", "-R", "-f", base_path],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    return result.returncode


def white_listed(url, white_listed_urls, white_listed_patterns):
    """
    check if link is in the white listed URLs or patterns to ignore.
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


def check_repo(file_paths, print_all, white_listed_urls, white_listed_patterns, retry_count=1, timeout=5):
    """
    check all urls extracted from all files in a repository.
    """
    # init results list (first is success, second is issue)
    check_results = [[], []]

    # loop files
    for file in file_paths:

        # collect links from each file
        urls = fileproc.collect_links_from_file(file)

        # eliminate white listed urls and white listed white listed patterns
        if len(white_listed_urls) > 0 or len(white_listed_patterns) > 0:
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
    """Derive the selected branch. We first look to the environment variable
       for INPUT_BRANCH, meaning that the user set the branch variable. If
       that is unset we parse GITHUB_REF. If both of those are unset,
       then we default to master.
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
    white_listed_urls = os.getenv("INPUT_WHITE_LISTED_URLS", "").split(",")
    white_listed_patterns = os.getenv("INPUT_WHITE_LISTED_PATTERNS", "").split(",")
    force_pass = os.getenv("INPUT_FORCE_PASS", "false").lower()
    retry_count = int(os.getenv("INPUT_RETRY_COUNT", 1))
    timeout = int(os.getenv("INPUT_TIMEOUT", 5)) # seconds

    # Are whitelisted urls provided, or an empty string?
    white_listed_urls = [x for x in white_listed_urls if x not in ["", None]]
    white_listed_patterns = [x for x in white_listed_patterns if x not in ["", None]]

    # clone project repo if defined
    base_path = os.environ.get("GITHUB_WORKSPACE", os.getcwd())

    # Alert user about settings
    print("  base path: %s" % base_path)
    print("   git path: %s" % git_path)
    print("  subfolder: %s" % subfolder)
    print("     branch: %s" % branch)
    print("    cleanup: %s" % cleanup)
    print(" file types: %s" % file_types)
    print("  print all: %s" % print_all)
    print("  whistlist: %s" % white_listed_urls)
    print("   patterns: %s" % white_listed_patterns)
    print(" force pass: %s" % force_pass)
    print("retry count: %s" % retry_count)
    print("    timeout: %s" % timeout)


    # If a custom base path is provided, clone and use it
    if git_path not in ["", None]:
        base_path = clone_repo(git_path, branch)

    if subfolder not in ["", None]:
        base_path = os.path.join(base_path, subfolder)

    # Assert that the base path exists
    if not os.path.exists(base_path):
        sys.exit("Cannot find %s to check" % base_path)

    # get all file paths
    file_paths = fileproc.get_file_paths(base_path, file_types)

    # check repo urls
    check_results = check_repo(file_paths, print_all, white_listed_urls,
                               white_listed_patterns, retry_count, timeout)

    # delete repo when done, if requested
    if cleanup == "true":
        del_repo(base_path)

    # exit
    if len(check_results) == 0:
        print("Done. No links were collected.")
        sys.exit(0)

    elif force_pass == "false" and len(check_results[1]) > 0 :
        print("Done. The following URLS did not pass:")
        print("\x1b[31m" + "\n".join(check_results[1]) + "\x1b[0m")
        sys.exit(1)

    else :
        print("Done. All URLS passed.")
        sys.exit(0)
