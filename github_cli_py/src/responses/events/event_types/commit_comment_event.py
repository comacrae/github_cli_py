from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base



class GithubCommitCommentPayload(event_base.GithubEventPayload):
  action:str
  comment: Mapping #TODO: make this more detailed by creating a commit class
  #https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28#get-a-commit

class GithubCommitCommentEvent(event_base.GithubEvent):
  payload: GithubCommitCommentPayload

  def to_cli_str(self)-> str:

    action:str = self.payload.action
    repo:str = self.repo.name
    return  f"Github commit comment {action} in {repo}"