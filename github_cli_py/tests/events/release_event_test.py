import pytest
from github_cli_py.src.responses.events.event_types import release_event
from github_cli_py.tests.events import generic


@pytest.mark.xfail
def test_init_success():
  generic.model_validate_and_assert_type(
    release_event.GithubReleaseEvent,
    "release_event_response.json"
  )
