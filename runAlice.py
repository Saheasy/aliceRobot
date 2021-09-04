import git
repo = git.Repo('aliceRobot')
repo.remotes.origin.pull()
