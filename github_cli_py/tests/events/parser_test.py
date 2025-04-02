import pytest
from github_cli_py.tests import utils
from github_cli_py.src.responses.events import parser
from github_cli_py.src.responses.events.event_types import create_event
from github_cli_py.src.responses.events.event_types import delete_event
from github_cli_py.src.responses.events.event_types import issue_comment_event
from github_cli_py.src.responses.events.event_types import issues_event
from github_cli_py.src.responses.events.event_types import pull_request_event
from github_cli_py.src.responses.events.event_types import event_base
from github_cli_py.src.responses.events.event_types import fork_event

@pytest.fixture
def parser_fixture():
  return parser.GithubEventParser()


def test_init_parser_success(parser_fixture: parser.GithubEventParser):
  return

@pytest.mark.parametrize("event_type,event_class",
                          [
                            ("create", create_event.GithubCreateEvent),
                            ("delete", delete_event.GithubDeleteEvent),
                            ("issue_comment", issue_comment_event.GithubIssueCommentEvent),
                            ("issues",issues_event.GithubIssuesEvent),
                            ("pull_request", pull_request_event.GithubPullRequestEvent)
                          ]
                        )
def test_parser_parse_reads_correct_type(
  event_type:str, 
  event_class: type[event_base.GithubEvent],
  parser_fixture: parser.GithubEventParser) -> None:
  filename:str =  event_type + "_event_response.json"
  assert type(filename) == str
  json:str = utils.load_json_resource(filename=filename)
  assert isinstance(parser_fixture.parse(json), event_class) 
  return
  


