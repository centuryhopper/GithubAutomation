from github import Github
from secrets import Secrets
import os, argparse




def main():
    g = Github(Secrets.githubAPIToken)

    # repos = g.search_repositories(query='language:python')
    # for repo in g.get_user().get_repos():
    #     print(repo.name)

    parser = argparse.ArgumentParser()
    parser.add_argument("--name", "-n", type=str,dest="name",required=True)
    parser.add_argument("--private", "-p", dest="isPrivate",action='store_true')
    args = parser.parse_args()
    repoName = args.name
    isPrivate = args.isPrivate

    # create a repo
    user = g.get_user()
    repo = user.create_repo(repoName,private=True if isPrivate else False)

    # creating local repository and connect with the created remote one from above
    try:
        REPO_PATH = Secrets.REPO_PATH # change this line to be your desired local repo path
        os.chdir(REPO_PATH)
        os.system(f'mkdir {repoName}')
        os.chdir(f'{REPO_PATH}{repoName}')
        os.system('git init')
        os.system(f'git remote add origin git@github.com:leozhang1/{repoName}.git') # change 'leozhang1' to your own github username
    #region files you want to add
        os.system(f"echo # {repoName} >> README.md")
        os.system("echo "" >> .gitignore")

    #endregion

# python automate_github.py --name OpenCV_Practice_In_C++ python -m venv virtenv
        os.system('git add .')
        os.system('git commit -m "Initial Commit"')
        os.system('git branch -m main')
        os.system('git push -u origin main')
    except FileExistsError as f:
        print(f)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    pass
    main()



