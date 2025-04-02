import pytest
from github_cli_py.src.responses.events import event_string_converter
from github_cli_py.src.responses.events.event_types import commit_comment_event, event_base

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