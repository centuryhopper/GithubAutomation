#!/usr/bin/env python3

import platform

if platform.system() == "Linux":
    import linux_tools as tools
elif platform.system() == "Windows":
    import windows_tools as tools

import requests
import argparse
import os
from dotenv import load_dotenv
load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str,dest="name",required=True)
parser.add_argument("--private", "-p", dest="isPrivate",action='store_true')

args = parser.parse_args()
repoName = args.name
isPrivate = args.isPrivate

apiUrl = 'https://api.github.com'
data = '{"name": "' + repoName + '", "private": true}' if isPrivate else '{"name": "' + repoName + '", "private": false}'

headers = {
    'Authorization': f'token {os.getenv("githubAPIToken")}',
    'Accept': 'application/vnd.github.v3+json'
}

# post request
try:
    r = requests.post(apiUrl + '/user/repos', data=data,headers=headers)
    r.raise_for_status()
    # pprint(r.json())
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
except Exception as e:
    print(e)

# creating local repository and connect with the created remote one from above
try:
    repoPath = tools.REPO_PATH
    os.chdir(repoPath)
    os.system(f'mkdir {repoName}')
    os.chdir(f'{repoPath}{repoName}')
    os.system('git init')
    os.system(f'git remote add origin git@github.com:leozhang1/{repoName}.git')
    os.system(f"echo '# {repoName}' >> README.md")
    os.system(f"echo '.DS_Store' >> .gitignore")
    os.system(f"echo '__pycache__' >> .gitignore")
    os.system(f"echo 'secrets.py' >> .gitignore")
    os.system('git add .')
    os.system("git commit -m 'Initial Commit'")
    os.system('git branch -m main')
    os.system('git push -u origin main')
    os.system('git checkout -b main_laptop')
    os.system('git push -u origin main_laptop')
except FileExistsError as f:
    print(f)
except Exception as e:
    print(e)

