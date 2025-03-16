import typing
import dataclasses
import pydantic

from github_cli_py.src.responses.events import event_base

@dataclasses.dataclass
class GithubPushEvent(event_base.GithubEvent):
  pass