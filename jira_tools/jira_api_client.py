from typing import Any, Dict, Protocol
from jira_tools.services.http import get_json

class JiraClientProtocol(Protocol):
    def get_issue_data(self, issue_key: str): ...
    def get_attachments(self, issue_key: str): ...
    def get_comments(self, issue_key: str): ...
    def delete_comment(self): ...

class JiraClient():
    def get_attachments(self, issue_key: str): ...
    def get_comments(self, issue_key: str): ...
    def delete_comment(self): ...
    def get_issue_data(self, issue_key: str) -> Dict[str, Any]:
        """
        Fetches a Robot Record (data attached to Jira issue) using the provided issue key.
        A Robot Record includes:
        1)
        2)
        3)
        Args:
            issue_key (str): The unique identifier for the Jira issue.
        Returns:
            dict: The Jira issue data parsed as a JSON object.
        """
        issue_url = f"{issue_key}"
        return get_json(issue_url)
