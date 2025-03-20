import pytest
from typing import Mapping
from github_cli_py.tests import utils
from github_cli_py.tests.events import generic
from github_cli_py.src.responses.events.event_types import pull_request_event

@pytest.fixture
def pull_request_response_json() -> Mapping:
  return utils.load_json_resource(filename="pull_request_event_response.json")

def test_init_success():
    generic.model_validate_and_assert_type(
    pull_request_event.GithubPullRequestEvent,
    filename="pull_request_event_response.json"
    )
    return


def test_init_pull_request_event_success(pull_request_response_json) -> None:
  event: pull_request_event.GithubPullRequestEvent = (
    pull_request_event.GithubPullRequestEvent.model_validate(pull_request_response_json)
  )
  assert type(event) == pull_request_event.GithubPullRequestEvent
