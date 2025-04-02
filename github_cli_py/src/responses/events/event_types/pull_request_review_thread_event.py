from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base

class GithubPullRequestReviewThreadEventPayload(event_base.GithubEventPayload):
  action:str
  pull_request: Mapping # TODO: create pull_request obj
  thread: Mapping #TODO: create comment obj

class GithubPullRequestReviewThreadEvent(event_base.GithubEvent):
  payload: GithubPullRequestReviewThreadEventPayload
  def to_cli_str(self) -> str:

    repo:str = self.repo.name
    action:str = self.payload.action
    return f"Pull request review thread {action} in {repo}"