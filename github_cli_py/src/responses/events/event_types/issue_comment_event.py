from typing import Mapping, Annotated, Optional
from pydantic import Field
from github_cli_py.src.responses.events.event_types import event_base

class IssueCommentEventPayload(event_base.GithubEventPayload):
  action: str
  changes: Mapping | None = None #TODO: create changes object
  issue: Mapping # TODO: create issue object
  comment: Mapping # TODO create comment object

class GithubIssueCommentEvent(event_base.GithubEvent):
  payload: IssueCommentEventPayload
