from typing import Mapping, Optional
import github_cli_py.src.responses.events.event_types as e
from github_cli_py.src.responses.events.event_types import event_base

class GithubParseResponseException(Exception):
  def __init__(self, message:str) -> None:
    self.message = message
class GithubEventParser():
  def __init__(self) -> None:
    self._event_map: Mapping = {
      "CreateEvent": e.create_event.GithubCreateEvent,
      "DeleteEvent": e.delete_event.GithubDeleteEvent, 
      "ForkEvent": e.fork_event.GithubForkEvent,
      "GollumEvent": e.gollum_event.GithubGollumEvent,
      "IssueCommentEvent": e.GithubIssueCommentEvent,
      "IssuesEvent": e.GithubIssuesCommentEvent,
      "PublicEvent": e.GithubPublicEvent,
      "PullRequestEvent": e.GithubPullRequestEvent,
      "PullRequestReviewEvent": e.GithubPullRequestReviewEvent,
      "PullRequestReviewComment": e.GithubPullRequestReviewCommentEvent,
      "PullRequestReviewThreadEvent": e.GithubPullRequestReviewThreadEvent,
      "PushEvent": e.GithubPushEvent,
      "ReleaseEvent": e.GithubReleaseEvent,
      "WatchEvent": e.GithubWatchEvent
    }
    return
  
  def parse(self, response_json:str) -> Optional[type[event_base.GithubEvent]]:
    try:
      event_type:str = response_json["type"]
    except KeyError:
      raise GithubParseResponseException("Event type key not found in response body")
    
    try:
      event_class: type[event_base.GithubEvent] = self._event_map[event_type]
    except KeyError:
      raise GithubParseResponseException(f"Event type {event_type} is invalid.")
    else:
      return event_class.model_validate_json(response_json)

    
      

