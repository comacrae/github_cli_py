from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base

class GithubPullRequestReviewEventPayload(event_base.GithubEventPayload):
  action: str
  pull_request: Mapping # TODO: create pull request obj
  review: Mapping #TODO : create review obj

class GithubPullRequestReviewEvent(event_base.GithubEvent):
  payload: GithubPullRequestReviewEventPayload