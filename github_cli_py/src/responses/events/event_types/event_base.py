import pydantic
import abc
from typing import Any


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
  payload:GithubEventPayload

  @classmethod
  @abc.abstractmethod
  def to_cli_str(self) -> str:
    pass





  
