from typing import Mapping
import github_cli_py.src.responses.events.event_types as e

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
  
  def 
