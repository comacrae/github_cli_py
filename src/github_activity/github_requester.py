from typing import Final
import dotenv
import requests
import os


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

    


    
  