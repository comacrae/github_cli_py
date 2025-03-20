import pytest
from typing import Mapping, Type
from github_cli_py.tests import utils
from github_cli_py.src.responses.events.event_types import event_base


def model_validate_and_assert_type(event_type: Type[event_base.GithubEvent],
                                    filename:str) -> event_base.GithubEvent:
  json_resource : Mapping = utils.load_json_resource(filename=filename)
  event: event_base.GithubEvent = event_type.model_validate(json_resource)
  assert type(event) == event_type
  return event