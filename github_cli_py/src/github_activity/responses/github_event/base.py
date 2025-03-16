from typing import Any, Mapping
import dataclasses
import abc

@dataclasses.dataclass
class Actor():
  id: int
  login: str
  display_login: str
  gravatar_id: str
  url: str
  avatar_url: str

@dataclasses.dataclass
class Repo():
  id : int
  name: str
  url: str

@dataclasses.dataclass
class Org():
  id: int
  login:str
  gravatar_id: str
  url:str
  avatar_url:str

@dataclasses.dataclass 
class GithubEvent(metaclass=abc.ABCMeta):
  id: int
  type:str
  actor: Actor 
  repo: Repo
  payload: Any # NOTE: This may change in the future
  public: bool
  created_at: str

  @abc.abstractmethod
  def parse_payload(payload:dict[str,Any]) -> Mapping:
    pass
  







  
