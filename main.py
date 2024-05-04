import time

import requests
from bs4 import BeautifulSoup 
import re

# with open("input.txt", "r") as f:
#     input_data = f.read().split("\n")
# 
# with open("docs_urls.txt", "w") as f:
#     for row in input_data:
#         if row != "":
#             url = re.search("<(.*?)>", row)
#             url = url.group()[:-1]
#             url = url[1:]
#             print(url)
#             f.write(url)
#             f.write("\n")
#         else:
#             f.write("\n")



with open("docs_urls.txt", "r") as f, open("github_urls.txt", "w") as fout:
    docs_urls_data = f.read().split("\n")
    for row in docs_urls_data:
        if row != "":
            print(f"fetching: {row}")
            resp = requests.get(row)
            if resp.status_code != 200:
                print(f"Received status: {resp.status_code}")
                continue
            soup = BeautifulSoup(resp.content, 'html5lib')
            try:
                # edit on github link
                github_url = "/".join(soup.find("a", attrs={"class": "fa-github"}).attrs.get("href").split("/")[:5])
            except AttributeError:
                try:
                    # download on github link
                    github_url = "/".join(soup.find("a", attrs={"class": "reference external"}, text="Download from GitHub").attrs.get("href").split("/")[:5])
                except AttributeError:
                    print("FAILED: {row}!")
            print(github_url)
            fout.write(github_url)
            fout.write("\n")
        else:
            fout.write("\n")
        time.sleep(0.5)
            
# resp = requests.get("https://docs.circuitpython.org/projects/adxl34x/en/latest/")
# soup = BeautifulSoup(resp.content, 'html5lib')
# 
# print("/".join(soup.find("a", attrs={"class": "fa-github"}).attrs.get("href").split("/")[:5]))