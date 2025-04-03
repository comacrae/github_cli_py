from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base

class MemberEventPayload(event_base.GithubEventPayload):
  action:str
  member: Mapping
  changes: Mapping


class GithubMemberEvent(event_base.GithubEvent):
  payload:MemberEventPayload

  def to_cli_str(self) -> str:
    action:str = self.payload.action
    repo:str = self.repo.name
    user:str = self.payload.member.login
    return  f"{str.capitalize(action)} {user} to {repo}"