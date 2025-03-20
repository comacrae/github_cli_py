from typing import Mapping
from github_cli_py.src.responses.events import event_base

class GithubPullRequestReviewThreadEventPayload(event_base.GithubEventPayload):
  action:str
  pull_request: Mapping # TODO: create pull_request obj
  thread: Mapping #TODO: create comment obj

class GithubPullRequestReviewThreadEvent(event_base.GithubEvent):
  payload: GithubPullRequestReviewThreadEventPayload