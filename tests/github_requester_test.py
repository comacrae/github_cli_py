import pytest
import typing
from github_activity import GithubRequester


def GithubRequester_init_is_valid_state_test() -> None:
  requester: GithubRequester = GithubRequester()
  assert GithubRequester.valid_connection() == True

  