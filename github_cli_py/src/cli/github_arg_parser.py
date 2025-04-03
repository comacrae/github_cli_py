import argparse
from github_cli_py.src.requester import github_requester

class GithubArgParser():
  def __init__(self):
    self.parser = argparse.ArgumentParser(prog='github-activity')
    self.parser.add_argument("username")
    self.parser.add_argument("--limit", default=10)
    self.requester = github_requester.GithubRequester()

  def parse(self):
    args = self.parser.parse_args()
    username = args.username
    if self.requester.user_exists(username):
      events = self.requester._get_public_user_events_paginated(username=username)
      for event in events:
        print(event.to_cli_str())

    else:
      print(f"User {username} does not exist")
    return
  