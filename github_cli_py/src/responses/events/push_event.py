from typing import Union, Mapping
import pydantic

from github_cli_py.src.responses.events import event_base

class PushEventPayload(pydantic.BaseModel):
  push_id: int
  size: int
  distinct_size: int 
  ref: str
  head: str
  before: str
  commits : list[Mapping[str,Union[str, dict,str,bool]]]


class GithubPushEvent(event_base.GithubEvent):
  payload: PushEventPayload
  