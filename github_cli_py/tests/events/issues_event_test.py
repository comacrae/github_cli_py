import pytest
from typing import Mapping
from github_cli_py.tests import utils
from github_cli_py.src.responses.events.event_types import issues_event

@pytest.fixture
def issues_event_response_json() -> Mapping:
  return utils.load_json_resource(filename="issues_event_response.json")

def test_issues_event_init_success(issues_event_response_json) -> None:
  event : issues_event.GithubIssuesEvent = (
    issues_event.GithubIssuesEvent.model_validate(issues_event_response_json)
  )
  assert type(event) == issues_event.GithubIssuesEvent
  return

