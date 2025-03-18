import pytest
from typing import Mapping
from github_cli_py.tests import utils
from github_cli_py.src.responses.events import public_event

@pytest.fixture
def public_event_response_json() -> Mapping:
  return utils.load_json_resource(filename="public_event_response.json")

@pytest.mark.xfail #TODO: Get public event api response json
def test_init_public_event_response_success(
    public_event_response_json) -> None:
  event: public_event.GithubPublicEvent = (
    public_event.GithubPublicEvent.model_validate(public_event_response_json)
  )
  assert type(event) == public_event.GithubPublicEvent
  return
