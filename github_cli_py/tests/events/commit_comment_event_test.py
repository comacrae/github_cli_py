import pytest
from github_cli_py.src.responses.events import commit_comment
from github_cli_py.tests import utils


@pytest.fixture
def commit_comment_json():
  return utils.load_json_resource("commit_comments_response.json")


def test_init_commit_comment_from_json_success():
  raise NotImplementedError