from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base

class SponsorshipEventPayload(event_base.GithubEventPayload):
  action:str
  effective_date: str
  changes: Mapping


class GithubSponsorshipEvent(event_base.GithubEvent):
  payload:SponsorshipEventPayload

  def to_cli_str(self) -> str:
    action:str = self.payload.action
    repo:str = self.repo.name
    eff_date:str = self.payload.effective_date
    return  f"{str.capitalize(action)} sponsorship event effective {eff_date} in {repo}"