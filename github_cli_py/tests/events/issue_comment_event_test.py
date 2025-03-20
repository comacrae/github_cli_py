import pytest
from typing import Mapping
from github_cli_py.tests import utils
from github_cli_py.src.responses.events.event_types import issue_comment_event

@pytest.fixture
def issue_comment_event_json() -> Mapping:
  return utils.load_json_resource(filename="issue_comment_event_response.json")

#@pytest.mark.xfail
def test_issue_comment_event_init_success(issue_comment_event_json):
  event: issue_comment_event.GithubIssueCommentEvent = (
    issue_comment_event.GithubIssueCommentEvent
    .model_validate(issue_comment_event_json)
  )
  assert type(event) == issue_comment_event.GithubIssueCommentEvent
