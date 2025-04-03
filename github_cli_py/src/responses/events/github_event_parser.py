import json
from typing import Mapping, Optional
from github_cli_py.src.responses.events.event_types import ( 
  event_base,
  create_event, 
  delete_event,
  fork_event,
  gollum_event,
  issue_comment_event,
  issues_event,
  public_event,
  pull_request_event,
  pull_request_review_event,
  pull_request_review_comment_event,
  pull_request_review_thread_event,
  push_event,
  release_event,
  watch_event,
  member_event,
  sponsorship_event,
  commit_comment_event
)

class GithubParseResponseException(Exception):
  def __init__(self, message:str) -> None:
    self.message = message
class GithubEventParser():
  def __init__(self) -> None:
    self._event_map: Mapping = {
      "MemberEvent": member_event.GithubMemberEvent,
      "SponsorshipEvent": sponsorship_event.GithubSponsorshipEvent,
      "CommitCommentEvent": commit_comment_event.GithubCommitCommentEvent,
      "CreateEvent": create_event.GithubCreateEvent,
      "DeleteEvent": delete_event.GithubDeleteEvent, 
      "ForkEvent": fork_event.GithubForkEvent,
      "GollumEvent": gollum_event.GithubGollumEvent,
      "IssueCommentEvent": issue_comment_event.GithubIssueCommentEvent,
      "IssuesEvent": issues_event.GithubIssuesEvent,
      "PublicEvent": public_event.GithubPublicEvent,
      "PullRequestEvent": pull_request_event.GithubPullRequestEvent,
      "PullRequestReviewEvent": pull_request_review_event.GithubPullRequestReviewEvent,
      "PullRequestReviewCommentEvent": pull_request_review_comment_event.GithubPullRequestReviewCommentEvent,
      "PullRequestReviewThreadEvent": pull_request_review_thread_event.GithubPullRequestReviewThreadEvent,
      "PushEvent": push_event.GithubPushEvent,
      "ReleaseEvent": release_event.GithubReleaseEvent,
      "WatchEvent": watch_event.GithubWatchEvent
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
      if type(response_json) == dict:
        response_json = json.dumps(response_json)
      return event_class.model_validate_json(response_json)

    
      

