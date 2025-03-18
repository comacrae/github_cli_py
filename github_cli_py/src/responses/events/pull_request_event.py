from typing import Mapping
from github_cli_py.src.responses.events import event_base

class GithubPullRequestEventPayload(event_base.GithubEventPayload):
  action:str
  number: int
  changes: Mapping | None = None # TODO: create changes obj
  pull_request: Mapping #TODO: create pull_request obj
  reason: str | None = None

class GithubPullRequestEvent(event_base.GithubEvent):
  payload: GithubPullRequestEventPayload
