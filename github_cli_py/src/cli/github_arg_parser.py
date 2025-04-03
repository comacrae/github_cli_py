from typing import Optional
import argparse
import getpass
from pathlib import Path
from github_cli_py.src.requester import github_requester

class GithubArgParser():
  def __init__(self):
    self.parser:argparse.ArgumentParser = argparse.ArgumentParser(prog='github-activity')
    self.requester: Optional[github_requester.GithubArgParser] = None
    self.parser.add_argument("username")
    self.parser.add_argument("-l",
                             "--limit", 
                             default=10, 
                             type=int,
                             help='the number of activities to pull for username'
                             )
    self.parser.add_argument(
                             "--keypath",
                             "-k",
                             default=None,
                             type=str,
                             help="The path to the file containing the API key"
                             )
    self.parser.add_argument(
                             "-i",
                             "--inputkey",
                             action='store_true',
                             help="Flag to indicate if you wish to enter your API key interactively")

  
  def load_api_key(self, file_path:str, inputkey:bool) -> Optional[str]:
    if file_path:
      api_key_file_path: Path = Path(file_path)
      if api_key_file_path.exists():
        with open(api_key_file_path,"r") as f:
          return f.readline()
    elif inputkey:
      return getpass.getpass("Enter API key:")
    else:
      return None



  def parse(self):
    args = self.parser.parse_args()
    username:str = args.username
    limit:int = args.limit
    keypath:str = args.keypath
    inputkey:bool = args.inputkey
    api_key:Optional[str] = self.load_api_key(keypath,inputkey)

    if api_key is None:
      print("Error: You must provide an API key interactively using -i or the API key filepath using -k")
    else:
      self.requester:github_requester.GithubRequester = github_requester.GithubRequester(api_key)
      if self.requester.valid_session() == True:
        self.print_events(username,limit)
      else:
        print(f"Error: API key invalid")


  def print_events(self, username:str, limit:int):
    if self.requester.user_exists(username):
        events = self.requester._get_public_user_events_paginated(username=username,
                                                                  limit=limit)
        if events is None:
          print("An error ocurred while parsing events")
        else:
          for event in events:
            print("- " + event.to_cli_str())
    else:
      print(f"User {username} does not exist")
    return