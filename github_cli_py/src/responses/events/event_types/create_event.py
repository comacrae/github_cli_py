from github_cli_py.src.responses.events.event_types import event_base

class CreateEventPayload(event_base.GithubEventPayload):
  ref:str | None
  ref_type:str
  master_branch:str
  description: str | None
  pusher_type:str

class GithubCreateEvent(event_base.GithubEvent):
  payload: CreateEventPayload

  def to_cli_str(self) -> str:
    ref_type:str = self.payload.ref_type
    master_branch:str = self.payload.master_branch
    repo:str = self.repo.name
    return  f"Github {ref_type} created in branch {master_branch} of {repo}"