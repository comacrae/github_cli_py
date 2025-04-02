import pytest
import json
from github_cli_py.src.responses.events import event_string_converter
from github_cli_py.src.responses.events.event_types import commit_comment_event, event_base, create_event
from github_cli_py.tests import utils

@pytest.fixture
def create_event_fixture() -> create_event.GithubCreateEvent:
  create_event_obj = utils.load_json_resource(filename="create_event_response.json")
  return create_event.GithubCreateEvent.model_validate(create_event_obj)

@pytest.fixture
def event_str_conv_fixture() -> event_string_converter.EventStringConverter:
  return event_string_converter.EventStringConverter()

@pytest.fixture
def github_event_base_fixture() -> event_base.GithubEvent:
  actor:event_base.GithubEventActor = event_base.GithubEventActor(
    id=1,login="test", display_login="test",gravatar_id="test",url="test",
    avatar_url="test"
  )

  repo:event_base.GithubEventRepo = event_base.GithubEventRepo(
    id=1, name="test", url="test"
  )

  payload: commit_comment_event.GithubCommitCommentPayload = (
    commit_comment_event.GithubCommitCommentPayload(
      action="push",
      comment={"test":"abc"}

    )
  )
  event:event_base.GithubEvent = event_base.GithubEvent(
    id=1, 
    type="test",
    actor=actor,
    repo=repo,
    public=False,
    created_at="test",
    payload=payload

  )

  return event

def test_event_str_conv_init_success(
    event_str_conv_fixture:event_string_converter.EventStringConverter,
    github_event_base_fixture:event_base.GithubEvent
    ):
  results:str = event_str_conv_fixture.convert(event=github_event_base_fixture)
  assert results == "Github event base: type test"

def test_create_event_conversion_success(
    event_str_conv_fixture:event_string_converter.EventStringConverter,
    create_event_fixture:create_event.GithubCreateEvent
  ):
  results:str = event_str_conv_fixture.convert(event=create_event_fixture)
  assert "created in branch" in results