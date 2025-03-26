import pydantic
from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base

class GithubIssuesEventPayload(event_base.GithubEventPayload):
  action:str
  issue: Mapping #TODO: create issues object
  changes: Mapping | None = None # TODO: create changes obj
  assignee : Mapping | None = None # TODO: create user assigned to issue
  label: Mapping | None = None #TODO: create label obj

class GithubIssuesEvent(event_base.GithubEvent):
  payload: GithubIssuesEventPayload