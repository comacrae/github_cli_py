import pydantic
import abc

from typing import Any, Mapping


class GithubEventPayload(pydantic.BaseModel, abc.ABC):
  pass

class GithubEventActor(pydantic.BaseModel):
  id: int
  login: str
  display_login: str
  gravatar_id: str
  url: str
  avatar_url: str

class GithubEventRepo(pydantic.BaseModel):
  id : int
  name: str
  url: str

class GithubEventOrg(pydantic.BaseModel):
  id: int
  login:str
  gravatar_id: str
  url:str
  avatar_url:str

class GithubEvent(pydantic.BaseModel,abc.ABC):
  id: int
  type:str
  actor: GithubEventActor
  repo: GithubEventRepo
  public: bool
  created_at: str

  @property
  @abc.abstractmethod
  def payload() -> GithubEventPayload:
    pass

  @abc.abstractmethod
  def parse_payload(payload:dict[str,Any]) -> GithubEventPayload:
    pass







  
