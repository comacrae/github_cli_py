from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base

class GithubWatchEventPayload(event_base.GithubEventPayload):
  action: str

class GithubWatchEvent(event_base.GithubEvent):
  payload: GithubWatchEventPayload

  def to_cli_str(self) -> str:
    repo:str = self.repo.name
    return f"Starred {repo}"