import pytest
from github_cli_py.tests.events import generic
from github_cli_py.src.responses.events import pull_request_review_comment_event

@pytest.mark.xfail # TODO: get response example
def test_init_success() -> None:
  generic.model_validate_and_assert_type(
    pull_request_review_comment_event.GithubPullRequestReviewCommentEvent,
    "pull_request_review_comment_event_response.json"
  )

