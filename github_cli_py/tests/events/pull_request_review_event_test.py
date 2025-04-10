import pytest
from github_cli_py.tests.events import generic
from github_cli_py.src.responses.events.event_types import pull_request_review_event

@pytest.mark.xfail
def test_init_success() -> None:
  generic.model_validate_and_assert_type(
    pull_request_review_event.GithubPullRequestReviewEvent,
    "pull_request_review_event_response.json"
  )
  return