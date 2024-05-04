import os

github_urls = None
with open("github_urls.txt") as github_urls_file:
    github_urls = github_urls_file.read().split("\n")

os.chdir("repo_workspace")

for url in github_urls:
    if url:  # weed out empty lines
        print(url)
        os.system(f"git clone {url}")
