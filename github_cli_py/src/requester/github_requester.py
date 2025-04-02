import dotenv
import requests
import os
from typing import Final
from github_cli_py.src.responses.events.event_types import event_base
from github_cli_py.src.responses.events import github_event_parser

class GithubRequester:
  """ Class for handling all interaction with the Github REST API. 
 
      Uses a requests.Session under the hood.

  Attributes:
    _GITHUB_API_KEY (Final[str]): Github API REST Key
    _session (requests.Session): Requests session object
  
  """

  def __init__(self) -> None:
    self._GITHUB_API_KEY : Final[str] = self._get_api_key()
    self._session : requests.Session = self._build_session()
    self._BASE_URL : Final[str] = "https://api.github.com/"
    return
  
  def _build_session(self) -> requests.Session:
    #Establish a session with github key as part of the header

    s: requests.Session = requests.Session()
    
    headers: dict[str,str] = {
      "Accept": "application/vnd.github+json",
      "Authorization": str(self._GITHUB_API_KEY),
      "X-Github-Api-Version":"2022-11-28",
      "User-Agent": "comacrae-github-cli-py-1.0"
    }

    s.headers = headers

    return s

  def _get_api_key(self) -> str:
    # Reads API key from local .env file
    load_success: bool = dotenv.load_dotenv()

    if(not load_success):
      raise FileNotFoundError(".env file not found in base repository")
    
    api_key :str | None  = os.getenv("GITHUB_API_KEY")

    if(api_key is None):
      raise RuntimeError("API key is None in _get_api_key")
    else:
      return api_key
  
  def _valid_session(self) -> bool:
    """ Returns a flag indicating whether the session is able to connect to 
    Github REST API
    """ 
    response: requests.Response = self._session.get(self._BASE_URL)
    return response.status_code == 200
  
  def _get_public_user_events_paginated(self,username: str, 
                                        page: int = 1, 
                                        per_page: int = 30
                                        ) -> list[event_base.GithubEvent]:
    """  Gets user response.Assumes the username has already been validated"""

    url : str = f"{self._BASE_URL}users/{username}/events/public"
    payload: dict[str,int] = {"page": page, "per_page": per_page}
    res : requests.Response = self._session.get(url=url, params=payload)
    parser:github_event_parser.GithubEventParser = github_event_parser.GithubEventParser()
    return [ parser.parse(event) for event in res.json()]

  
  def user_exists(self,username:str) -> bool:
    """ Checks to confirm whether a username in Github eists"""
    url:str = f"{self._BASE_URL}users/{username}"    
    res: requests.Response = self._session.get(url=url)
    return res.status_code == 200
  



    


    
  