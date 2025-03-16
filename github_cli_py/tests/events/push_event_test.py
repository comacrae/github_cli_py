import pytest
import json
from typing import Mapping
from github_cli_py.src.requester import github_requester
from github_cli_py.src.responses.events import github_event

@pytest.fixture
def requester() -> github_requester.GithubRequester:
  return requester.Requester()


@pytest.fixture
def push_event_json() -> Mapping:
  with open(r"C:\Users\comac\github_cli_py\github_cli_py\tests\docs\users_events_public_response.json", "r") as f:
    push_event: Mapping =  json.load(f)[0]
    assert push_event["type"] == "PushEvent"
    return push_event

def test_push_event_init_success() -> None:
  raise NotImplementedErro
