Inspired by the author of this video: https://www.youtube.com/watch?v=b3ySWJinSh4

## Thanks for using my script! It is fulfilling to know that I can make someone else's life easier with this automation script

Directions:
* make sure you have all the dependencies you need in this virtual environment by typing ```pip install -r requirements.txt```
* to create a public repo: ```python automate_github.py --name [YourRemoteRepoName]```
* to create a private repo: ```python automate_github.py --name [YourRemoteRepoName] --private```

## The secrets.py module that I have imported is just my own personal information that I don't want to show to the public!
## What I can show is the boilerplate, so you can add your own (just don't forget to add secrets.py to your gitignore so you don't share information such as your git hub password to the public)
secrets.py boilerplate
```
class Secrets:
    user='[YourGithubUserName]'
    password='[YourGithubPassword]'
    apiKey='[YourGithubAPiKey]' (if you don't know what this is, I would suggest doing some research on the internet. Here's one helpful video https://www.youtube.com/watch?v=b3ySWJinSh4&t=404s)
    repoPath='[YourLocalRepositoryPath]'
```

## Now you just have to go inside the automate_github.py script and add your own local repository path (directions are shown in comments in the script)

## Enjoy!
