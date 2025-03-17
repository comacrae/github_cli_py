import pytest
from typing import Mapping
from github_cli_py.src.responses.events import delete_event
from github_cli_py.tests import utils as test_utils

@pytest.fixture
def json_resource() -> Mapping:
  return test_utils.load_json_resource(filename="delete_event_response.json")

def test_init_delete_event_success(json_resource) -> None:
  event: delete_event.GithubDeleteEvent = (
    delete_event.GithubDeleteEvent.model_validate(json_resource)
  )