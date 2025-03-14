import pytest
import typing
import os
from dotenv import load_dotenv
from github_activity import GithubRequester


class GithubRequesterTests:
  def init_in_valid_state_test() -> None:
    requester: GithubRequester = GithubRequester()
    assert GithubRequester.valid_connection() == True

  def get_api_key_success() -> None:
    load_dotenv()
    api_key: str = os.getenv("GITHUB_API_KEY")
    requester: GithubRequester = GithubRequester()
    assert api_key == requester._session.headers["Authorization"]
    
    

  