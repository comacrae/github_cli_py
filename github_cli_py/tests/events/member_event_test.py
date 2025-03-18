import pytest
from typing import Mapping
from github_cli_py.src.responses.events import member_event
from github_cli_py.tests import utils

@pytest.fixture
def member_event_response_json() -> Mapping:
  return utils.load_json_resource(filename="member_event_response.json")

@pytest.mark.xfail # TODO: get api test file
def test_init_member_event_init_success(member_event_response_json) -> None:
  event: member_event.GithubMemberEvent = (
    member_event.GithubMemberEvent.model_validate(member_event_response_json)
    )
  assert type(event) == member_event.GithubMemberEvent
  return