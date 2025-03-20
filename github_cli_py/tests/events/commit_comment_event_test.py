import pytest
from github_cli_py.src.responses.events.event_types import commit_comment_event
from github_cli_py.tests import utils



@pytest.mark.xfail
def test_init_commit_comment_from_json_success(commit_comment_json):
  return
