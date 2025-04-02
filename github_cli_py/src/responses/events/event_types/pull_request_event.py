from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base

class GithubPullRequestEventPayload(event_base.GithubEventPayload):
  action:str
  number: int
  changes: Mapping | None = None # TODO: create changes obj
  pull_request: Mapping #TODO: create pull_request obj
  reason: str | None = None

class GithubPullRequestEvent(event_base.GithubEvent):
  payload: GithubPullRequestEventPayload
  def to_cli_str(self) -> str:
    repo:str = self.repo.name
    action:str = self.payload.action
    return f"Pull request {action} in {repo}"