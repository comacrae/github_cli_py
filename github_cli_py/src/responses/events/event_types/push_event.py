from typing import Union, Mapping
import pydantic

from github_cli_py.src.responses.events import event_base

class GithubCommitAuthor(pydantic.BaseModel):
  email:str
  name:str

class GithubCommit(pydantic.BaseModel):
  sha:str
  message:str
  author:GithubCommitAuthor
  distinct: bool
  message: str
  sha: str
  url: str


class PushEventPayload(event_base.GithubEventPayload):
  push_id: int
  size: int
  distinct_size: int 
  ref: str
  head: str
  before: str
  commits : list[GithubCommit]


class GithubPushEvent(event_base.GithubEvent):
  payload: PushEventPayload
  