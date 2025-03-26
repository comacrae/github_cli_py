import pytest
from github_cli_py.tests import utils
from github_cli_py.src.responses.events import parser
from github_cli_py.src.responses.events.event_types import (
  event_base, 
  create_event,
  delete_event,
  issue_comment_event,
  issues_event,
  pull_request_event)

@pytest.fixture
def parser_fixture():
  return parser.GithubParser()


def test_init_parser_success(parser_fixture: parser.EventParser):
  return

@pytest.mark.parametrize("json_path,event_class",
                          [("create", create_event.GithubCreateEvent),
                          ("delete", delete_event.GithubDeleteEvent),
                          ("issue_comment", issue_comment_event.GithubIssueCommentEvent),
                          ("issues", issues_event.GithubIssuesEvent),
                          ("pull_request", pull_request_event.GithubPullRequestEvent)])
def test_parser_parse_reads_correct_type(
  event_type:str, 
  event_class: type[event_base.GithubEvent],
  parser_fixture: parser.EventParser) -> None:
  json:str = utils.load_json_resource(f"{event_type}_event_response.json")
  assert type(parser_fixture.parse(json)) == event_class
  return
  


