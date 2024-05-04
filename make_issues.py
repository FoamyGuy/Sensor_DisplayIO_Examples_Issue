
import os
import time

repo_dirs = os.listdir("repo_workspace")

os.chdir("repo_workspace")

for repo in repo_dirs:
    os.chdir(repo)
    print(f"{repo} - {os.getcwd()}")
    #print("would run os.system('../../make_issue.sh')")
    print("running make_issue.sh")
    os.system("../../make_issue.sh")
    os.chdir("../")
    time.sleep(2)