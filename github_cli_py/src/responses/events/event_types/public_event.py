from github_cli_py.src.responses.events.event_types import event_base

class GithubPublicEvent(event_base.GithubEvent):
  payload: None

  def to_cli_str(self) -> str:

    repo:str = self.repo.name
    return f"{repo} made public"