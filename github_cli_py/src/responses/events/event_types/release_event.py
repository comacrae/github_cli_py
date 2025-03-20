from typing import Mapping
from github_cli_py.src.responses.events import event_base

class GithubReleaseEventPayload(event_base.GithubEventPayload):
  action: str
  changes: Mapping | None = None #TODO: create changes class
  release: Mapping # TODO: create release class

class GithubReleaseEvent(event_base.GithubEvent):
  payload: event_base.GithubEventPayload