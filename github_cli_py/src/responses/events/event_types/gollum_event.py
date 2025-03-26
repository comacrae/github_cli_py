import pydantic
from github_cli_py.src.responses.events.event_types import event_base

class WikiPage(pydantic.BaseModel):
  page_name: str
  title: str
  action: str
  sha: str
  html_url: str


class GollumEventPayload(event_base.GithubEventPayload):
  pages: list[WikiPage]

class GithubGollumEvent(event_base.GithubEvent):
  payload: GollumEventPayload