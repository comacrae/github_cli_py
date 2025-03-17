from github_cli_py.src.responses.events import event_base

class CreateEventPayload(event_base.GithubEventPayload):
  ref:str | None
  ref_type:str
  master_branch:str
  description: str | None
  pusher_type:str

class GithubCreateEvent(event_base.GithubEvent):
  payload: CreateEventPayload