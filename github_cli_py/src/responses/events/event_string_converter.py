from typing import Mapping
from github_cli_py.src.responses.events.event_types import event_base
from github_cli_py.src.responses.events.event_types import commit_comment_event
from github_cli_py.src.responses.events.event_types import create_event
from github_cli_py.src.responses.events.event_types import delete_event
from github_cli_py.src.responses.events.event_types import fork_event
from github_cli_py.src.responses.events.event_types import gollum_event
from github_cli_py.src.responses.events.event_types import issue_comment_event
from github_cli_py.src.responses.events.event_types import issues_event
from github_cli_py.src.responses.events.event_types import public_event
from github_cli_py.src.responses.events.event_types import pull_request_event
from github_cli_py.src.responses.events.event_types import pull_request_review_comment_event
from github_cli_py.src.responses.events.event_types import pull_request_review_event
from github_cli_py.src.responses.events.event_types import pull_request_review_thread_event
from github_cli_py.src.responses.events.event_types import push_event
from github_cli_py.src.responses.events.event_types import release_event
from github_cli_py.src.responses.events.event_types import watch_event

"""
commit_comment_event.GithubCommitCommentEvent: self.print_commit_comment_event,
create_event.GithubCreateEvent:self.print_create_event,
delete_event.GithubDeleteEvent:self.print_delete_event,
fork_event.GithubForkEvent:self.print_fork_event,
gollum_event.GithubGollumEvent:self.print_gollum_event,
issue_comment_event.GithubIssueCommentEvent:self.print_issue_comment_event,
issues_event.GithubIssuesEvent: self.print_issues_event,
public_event.GithubPublicEvent:self.print_public_event,
pull_request_event.GithubPullRequestEvent:self.print_pull_request_event,
pull_request_review_comment_event.GithubPullRequestReviewCommentEvent:self.print_pull_request_review_comment_event,
pull_request_review_event.GithubPullRequestReviewEvent:self.print_pull_request_review_event,
pull_request_review_thread_event.GithubPullRequestReviewThreadEvent:self.print_pull_request_review_thread_event,
push_event.PushEventPayload:self.print_push_event,
release_event.GithubReleaseEvent:self.print_release_event,
watch_event.GithubWatchEvent:self.print_watch_event
"""

class EventStringConverter():
  def __init__(self):
   self.func_map: Mapping = {
      event_base.GithubEvent: self.event_base_to_str
   }

  def event_base_to_str(self, event:event_base.GithubEvent) -> str:
    return f"Github event base: type {event.type}"
  
  def convert(self, event:event_base.GithubEvent) -> str:
    conversion_func = self.func_map[type(event)]
    return conversion_func(event)
