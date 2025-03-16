import pytest
import os
import dotenv
from github_cli_py.src.requester import github_requester 

@pytest.fixture
def requester() -> github_requester.GithubRequester :
  return github_requester.GithubRequester()


class TestGithubRequester:

  def test_init_in_valid_state(self, 
                               requester: github_requester.GithubRequester
                               ) -> None:
    assert requester._valid_session() == True
    return
  
#TODO: Add a test that checks for error handling when an API KEY isn't available

  def test_get_api_key_success(
      self, 
      requester: github_requester.GithubRequester
      ) -> None:
    dotenv.load_dotenv() 
    api_key: str | None = os.getenv("GITHUB_API_KEY")
    assert api_key == requester._session.headers["Authorization"]
    return
  
  def test_get_events_valid_username_returns_valid_response(
      self, 
      requester: github_requester.GithubRequester
      ) -> None:
    requester._get_public_user_events_paginated(
      username = "comacrae", page=1, per_page=30
      )
    return
  
  def test_get_user_invalid_username_returns_false(
      self, 
      requester: github_requester.GithubRequester
      ) -> None:
    assert False == requester.user_exists(
      username="This_username_does_not_exist"
      ) 

    
    

  