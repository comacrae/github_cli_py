import pytest
import typing
import os
import dotenv
import github_activity # https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html#choosing-a-test-layout-import-rules


class GithubRequesterTests:

  def test_init_in_valid_state(self) -> None:
    requester: github_activity.github_requester.GithubRequester = github_activity.github_requester.GithubRequester()
    assert requester.valid_connection() == True

  def get_api_key_success(self) -> None:
    dotenv.load_dotenv() 
    api_key: str | None = os.getenv("GITHUB_API_KEY")
    requester: github_activity.github_requester.GithubRequester = github_activity.github_requester.GithubRequester()
    assert api_key == requester._session.headers["Authorization"]
    
    

  