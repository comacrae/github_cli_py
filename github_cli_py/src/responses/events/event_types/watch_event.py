from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base

class GithubWatchEventPayload(event_base.GithubEventPayload):
  action: str

class GithubWatchEvent(event_base.GithubEvent):
  payload: GithubWatchEventPayload