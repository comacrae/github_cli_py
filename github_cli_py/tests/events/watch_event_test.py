import pytest
from github_cli_py.src.responses.events.event_types import watch_event
from github_cli_py.tests.events import generic

@pytest.mark.xfail # TODO: get example response
def init_test_success():
  generic.model_validate_and_assert_type(
    watch_event.GithubWatchEvent,
    "watch_event_response.json"
  )
