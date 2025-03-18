import pytest
from github_cli_py.tests import utils
from github_cli_py.src.responses.events import gollum_event

@pytest.fixture
def gollum_response_json():
  return utils.load_json_resource(filename="gollum_event_response.json")

def test_gollum_event_init_success(gollum_response_json) -> None:

  event: gollum_event.GithubGollumEvent = (
    gollum_event.GithubGollumEvent.model_validate(gollum_response_json)
  )

  assert type(event) == gollum_event.GithubGollumEvent

  return

