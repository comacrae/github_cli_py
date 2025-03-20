import pytest
from typing import Mapping
from github_cli_py.src.responses.events.event_types import create_event
from github_cli_py.tests import utils as test_utils

@pytest.fixture
def json_resource() -> Mapping:
  return test_utils.load_json_resource(filename="create_event_response.json")

def test_init_create_event_success(json_resource) -> None:
  event: create_event.GithubCreateEvent = (
    create_event.GithubCreateEvent.model_validate(json_resource)
  )
  assert type(event) == create_event.GithubCreateEvent
    