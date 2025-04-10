from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base

class GithubReleaseEventPayload(event_base.GithubEventPayload):
  action: str
  changes: Mapping | None = None #TODO: create changes class
  release: Mapping # TODO: create release class

class GithubReleaseEvent(event_base.GithubEvent):
  payload: event_base.GithubEventPayload

  def to_cli_str(self)-> str:

    repo:str = self.repo.name
    return f"Published {repo}"