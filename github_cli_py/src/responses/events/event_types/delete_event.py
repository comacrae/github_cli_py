from typing import Mapping
from github_cli_py.src.responses.events import event_base

class DeleteEventPayload(event_base.GithubEventPayload):
  ref: str
  ref_type: str

class GithubDeleteEvent(event_base.GithubEvent):
  payload:DeleteEventPayload