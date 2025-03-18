import pydantic
from github_cli_py.src.responses.events import event_base

class WikiPage(pydantic.BaseModel):
  page_name: str
  title: str
  action: str
  sha: str
  html_url: str


class GollumPayload(event_base.GithubEventPayload):
  pages: list[WikiPage]

class GithubGollumEvent(event_base.GithubEvent):
  payload: GollumPayload