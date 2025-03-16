from typing import Any, Mapping
import dataclasses
import abc


class GithubEventPayload(metaclass=abc.ABCMeta):
  pass

@dataclasses.dataclass
class GithubEventActor():
  id: int
  login: str
  display_login: str
  gravatar_id: str
  url: str
  avatar_url: str

@dataclasses.dataclass
class GithubEventRepo():
  id : int
  name: str
  url: str

@dataclasses.dataclass
class GithubEventOrg():
  id: int
  login:str
  gravatar_id: str
  url:str
  avatar_url:str

@dataclasses.dataclass 
class GithubEvent(metaclass=abc.ABCMeta):
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
  







  
