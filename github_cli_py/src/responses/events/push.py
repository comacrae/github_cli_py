import typing
import dataclasses
import pydantic

from github_cli_py.src.responses.events import base

@dataclasses.dataclass
class GithubPushEvent(base.GithubEvent):
  pass