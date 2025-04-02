from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base

class DeleteEventPayload(event_base.GithubEventPayload):
  ref: str
  ref_type: str

class GithubDeleteEvent(event_base.GithubEvent):
  payload:DeleteEventPayload

  def to_cli_str(self) -> str:
    ref_type: str = self.payload.ref_type
    repo:str = self.repo.name
    return  f"Deleted {ref_type} in {repo}"