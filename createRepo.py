#!/usr/bin/env python3

import requests
import argparse
import os
from pprint import pprint
from secrets import githubAPIToken

parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str,dest="name",required=True)
parser.add_argument("--private", "-p", dest="isPrivate",action='store_true')

args = parser.parse_args()
repoName = args.name
isPrivate = args.isPrivate

apiUrl = 'https://api.github.com'
data = '{"name": "' + repoName + '", "private": true}' if isPrivate else '{"name": "' + repoName + '", "private": false}'

headers = {
    'Authorization': f'token {githubAPIToken}',
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
    repoPath = '/Users/leozhang/Documents/GitHub/'
    os.chdir(repoPath)
    os.system(f'mkdir {repoName}')
    os.chdir(f'{repoPath}{repoName}')
    os.system('git init')
    os.system(f'git remote add origin https://github.com/leozhang1/{repoName}.git')
    os.system(f"echo '# {repoName}' >> README.md")
    os.system('git add .')
    os.system("git commit -m 'Initial Commit'")
    os.system('git branch -m main')
    os.system('git push -u origin main')
    os.system('git checkout -b main_macos')
    os.system('git push -u origin main_macos')
except FileExistsError as f:
    print(f)
except Exception as e:
    print(e)

