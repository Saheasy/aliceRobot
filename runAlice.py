import git
repo = git.Repo('aliceRobot')
repo.remotes.origin.pull()
exec(open("aliceRobot/main.py").read())