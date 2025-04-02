from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base

class GithubPullRequestReviewCommentEventPayload(event_base.GithubEventPayload):
  action:str
  changes: Mapping | None = None #TODO: create changes obj
  pull_request: Mapping # TODO: create pull_request obj
  comment: Mapping #TODO: create comment obj

class GithubPullRequestReviewCommentEvent(event_base.GithubEvent):
  payload: GithubPullRequestReviewCommentEventPayload
  def to_cli_str(self) -> str:
    repo:str = self.repo.name
    action:str = self.payload.action
    return f"Pull request review {action} in {repo}"