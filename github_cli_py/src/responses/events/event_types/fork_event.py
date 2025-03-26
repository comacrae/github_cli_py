from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base

class ForkEventPayload(event_base.GithubEventPayload):
  forkee: Mapping # TODO: Make repository resource class

class GithubForkEvent(event_base.GithubEvent):
  payload:ForkEventPayload
  #https://docs.github.com/en/rest/using-the-rest-api/github-event-types?apiVersion=2022-11-28#forkevent