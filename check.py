import os
import urlproc
import fileproc

git_path = os.getenv("INPUT_GIT_PATH", "")
file_types = os.getenv("INPUT_FILE_TYPES", "").split(",")
print_all = os.getenv("INPUT_PRINT_ALL", "")
print("Inputs: ", git_path, file_types, print_all)

base_path = os.path.basename(git_path)
os.system(f"git clone {git_path} {base_path}")

# get all file paths
file_paths = fileproc.get_file_paths(base_path, file_types)

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
os.system(f"rm -R -f {base_path}")
print("Done.")
