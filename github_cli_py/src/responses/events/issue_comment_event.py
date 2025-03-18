from typing import Mapping
from github_cli_py.src.responses.events import event_base

class IssueCommentPayload(event_base.GithubEventPayload):
  action: str
  changes: Mapping | None #TODO: create changes object
  issue: Mapping # TODO: create issue object
  comment: Mapping # TODO create comment object

class GithubIssueCommentEvent(event_base.GithubEvent):
  payload: IssueCommentPayload
