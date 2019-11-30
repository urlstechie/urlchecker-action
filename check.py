#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from core import urlproc
from core import fileproc


def clone_rep(git_path):
    """
    clone and name a git repository.
    """
    base_path = os.path.basename(git_path)
    try:
        os.system("git clone " + git_path + " " + base_path)
        return True
    except:
        return False


def del_repo(base_path):
    """
    delete repository.
    """
    try:
        os.system("rm -R -f " + base_path)
        return True
    except:
        return False


def check_repo(file_paths, print_all):
    """
    check all urls extracted from all files in a repository.
    """
    # loop files
    for file in file_paths:

        # collect links from each file
        urls = fileproc.collect_links_from_file(file)

        # if some links are found, check them
        if urls != []:
            print("\n", file, "\n", "-" * len(file))
            urlproc.check_urls(file, urls)

        # if no urls are found, mention it if required
        else:
            if print_all == "True":
                print("\n", file, "\n", "-" * len(file))
                print("No urls found.")


if __name__ == "__main__":

    # read input variables
    git_path = os.getenv("INPUT_GIT_PATH", "")
    file_types = os.getenv("INPUT_FILE_TYPES", "").split(",")
    print_all = os.getenv("INPUT_PRINT_ALL", "")

    # clone project repo
    cloning_status = clone_repo(git_path)

    # get all file paths
    file_paths = fileproc.get_file_paths(base_path, file_types)

    # check repo urls
    check_repo(file_paths)

    # delete repo when done
    deletion_status = del_repo(base_path)
    print("Done.")
