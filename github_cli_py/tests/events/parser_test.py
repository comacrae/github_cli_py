import pytest
from github_cli_py.src.responses.events import parser

@pytest.fixture
def parser_fixture():
  return parser.GithubParser()

def test_init_parser_success(parser_fixture: parser.EventParser):
  return
