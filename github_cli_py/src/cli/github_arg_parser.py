import argparse
from github_cli_py.src.requester import github_requester

class GithubArgParser():
  def __init__(self):
    self.parser = argparse.ArgumentParser(prog='github-activity')
    self.parser.add_argument("username")

  def parse(self):
    args = self.parser.parse_args()
    username = args.username
    print(username)
    return
  