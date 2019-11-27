import os
import urlproc
import fileproc

base_path = os.getenv("BASE_PATH", "")
file_types = os.getenv("FILE_TYPES", "").split(",")
print_all = os.getenv("PRINT_ALL", "")

print(base_path, file_types, print_all)

# get all file paths
file_paths = fileproc.get_file_paths(base_path, file_types)
print("file_paths: ", file_paths)

file_paths = ["https://github.com/SuperKogito/SuperKogito.github.io/blob/master/_project/docs/source/index.rst"]

import requests
text = requests.get(filepath).text
print(text)

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
        if print_all == True:
            print("\n", file, "\n", "-" * len(file))
            print("No urls found.")

# print done to mark end of script
print("Done.")
