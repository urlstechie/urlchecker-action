import requests
from termcolor import colored

long_url = str(max([len(url) for url in urls]))
print(long_url)
s = "%"+long_url+"s %10s"
print(s)

for url in [url for url in urls if "http" in url]:
    request = requests.get(url)
    if request.status_code == 200:
        print(s % (url, colored("URL works", "green")))
    else:
        # Do something when request fails
        print(s % (url, colored("URL borkne", "red")))
