import git
repo = git.Repo('gitAlice')
repo.remotes.origin.pull()
exec(open("gitAlice/main.py").read())