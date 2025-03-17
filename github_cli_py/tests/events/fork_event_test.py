import pytest
from typing import Mapping
from github_cli_py.src.responses.events import fork_event
from github_cli_py.tests import utils


@pytest.fixture
def fork_event_response_json() -> Mapping: 
  return utils.load_json_resource(filename="fork_event_response.json")

@pytest.mark.xfail
def test_init_commit_comment_from_json_success(fork_event_reponse_json: Mapping):
  #https://docs.github.com/en/rest/using-the-rest-api/github-event-types?apiVersion=2022-11-28#forkevent
  return