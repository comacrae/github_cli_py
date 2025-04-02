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


class EventStringConverter():
  def __init__(self):
   self.func_map: Mapping = {
      event_base.GithubEvent: self.event_base_to_str,
      commit_comment_event.GithubCommitCommentEvent: self.commit_comment_event_to_str,
      create_event.GithubCreateEvent:self.create_event_to_str,
      delete_event.GithubDeleteEvent:self.delete_event_to_str,
      fork_event.GithubForkEvent:self.fork_event_to_str,
      gollum_event.GithubGollumEvent:self.gollum_event_to_str,
      issue_comment_event.GithubIssueCommentEvent:self.issue_comment_event_to_str,
      issues_event.GithubIssuesEvent: self.issues_event_to_str,
      public_event.GithubPublicEvent:self.public_event_to_str,
      pull_request_event.GithubPullRequestEvent:self.pull_request_event_to_str,
      pull_request_review_comment_event.GithubPullRequestReviewCommentEvent:self.pull_request_review_comment_event_to_str,
      pull_request_review_event.GithubPullRequestReviewEvent:self.pull_request_review_event_to_str,
      pull_request_review_thread_event.GithubPullRequestReviewThreadEvent:self.pull_request_review_thread_event_to_str,
      push_event.PushEventPayload:self.push_event_to_str,
      release_event.GithubReleaseEvent:self.release_event_to_str,
      watch_event.GithubWatchEvent:self.watch_event_to_str
   }

  def event_base_to_str(self, event:event_base.GithubEvent) -> str:
    return f"Github event base: type {event.type}"

  def create_event_to_str(self, event:create_event.GithubCreateEvent) -> str:
    repo:str = event.repo.name
    ref_type:str = event.payload.ref_type
    master_branch:str = event.payload.master_branch
    return  f"Github {ref_type} created in branch {master_branch} of {repo}"
  
  def commit_comment_event_to_str(self, 
                                  event:commit_comment_event.GithubCommitCommentEvent) -> str:  
    action:str = event.payload.action
    repo:str = event.repo.name
    return  f"Github commit comment {action} in {repo}"

  def delete_event_to_str(self, 
                                  event:delete_event.GithubDeleteEvent) -> str:  
    ref_type: str = event.payload.ref_type
    repo:str = event.repo.name
    return  f"Deleted {ref_type} in {repo}"

  def fork_event_to_str(self, 
                                  event:fork_event.GithubForkEvent) -> str:  
    repo:str = event.repo.name
    return  f"Forked {repo}"
                                  

  def gollum_event_to_str(self, 
                                  event:gollum_event.GithubGollumEvent) -> str:  
    repo:str = event.repo.name
    return  f"Gollum event in {repo}"

  def issue_comment_event_to_str(self, 
                                  event:issue_comment_event.GithubIssueCommentEvent) -> str:  
    action:str = event.payload.action
    repo:str = event.repo.name
    return f"Issue comment {action} in {repo}"


  def issues_event_to_str(self, 
                                  event:issues_event.GithubIssuesEvent) -> str:  
    action:str = event.payload.action
    repo:str = event.repo.name
    return f"Issue {action} in {repo}"

  def public_event_to_str(self, 
                                  event:public_event.GithubPublicEvent) -> str:  
    repo:str = event.repo.name
    return f"{repo} made public"

  def pull_request_event_to_str(self, 
                                  event:pull_request_event.GithubPullRequestEvent) -> str:  
    repo:str = event.repo.name
    action:str = event.payload.action
    return f"Pull request {action} in {repo}"
  
  def pull_request_review_event_to_str(self, 
                                  event:pull_request_review_event.GithubPullRequestReviewEvent) -> str:  
    repo:str = event.repo.name
    action:str = event.payload.action
    return f"Pull request review {action} in {repo}"

  def pull_request_review_comment_event_to_str(self, 
                                  event:pull_request_review_comment_event.GithubPullRequestReviewCommentEvent) -> str:  
    repo:str = event.repo.name
    action:str = event.payload.action
    return f"Pull request review comment {action} in {repo}"
  def pull_request_review_thread_event_to_str(self, 
                                  event:pull_request_review_thread_event.GithubPullRequestReviewThreadEvent) -> str:  
    repo:str = event.repo.name
    action:str = event.payload.action
    return f"Pull request review thread {action} in {repo}"

  def push_event_to_str(self, 
                                  event:push_event.GithubPushEvent) -> str:  
    repo:str = event.repo.name
    size:int = event.payload.size
    return f"Pushed {size} commits to {repo}"

  def release_event_to_str(self, 
                                  event:release_event.GithubReleaseEvent) -> str:  
    repo:str = event.repo.name
    return f"Published {repo}"

  def watch_event_to_str(self, 
                                  event:watch_event.GithubWatchEvent) -> str:  
    repo:str = event.repo.name
    return f"Starred {repo}"

  def convert(self, event:event_base.GithubEvent) -> str:
    conversion_func = self.func_map[type(event)]
    return conversion_func(event)
