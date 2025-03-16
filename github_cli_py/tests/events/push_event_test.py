import pytest
import json
from typing import Mapping
from github_cli_py.src.requester import github_requester
from github_cli_py.src.responses.events import push_event

@pytest.fixture
def requester() -> github_requester.GithubRequester:
  return requester.Requester()


@pytest.fixture
def push_event_json() -> Mapping:
  with open(r"C:\Users\comac\github_cli_py\github_cli_py\tests\resources\users_events_public_response.json", "r") as f:
    push_event: Mapping =  json.load(f)[0]
    assert push_event["type"] == "PushEvent"
    return push_event

@pytest.fixture
def push_event_fixture(push_event_json: Mapping) -> push_event.GithubPushEvent:
  return push_event.GithubPushEvent.model_validate(push_event_json)

@pytest.fixture
def push_event_commits(push_event_fixture: push_event.GithubPushEvent) -> list[push_event.GithubCommit]:
  return push_event_fixture.payload.commits



def test_push_event_init_success(push_event_json) -> None:
  event: push_event.GithubPushEvent = push_event.GithubPushEvent.model_validate(push_event_json)
  assert type(event) == push_event.GithubPushEvent
  assert type(event.id) == int
  assert event.id == int(push_event_json["id"])

def test_push_event_commits_valid(push_event_commits: list[push_event.GithubCommit]) -> None:
  for commit in push_event_commits:
    assert type(commit) == push_event.GithubCommit
    assert commit.author.name == "comacrae"


