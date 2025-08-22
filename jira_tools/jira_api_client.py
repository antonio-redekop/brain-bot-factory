from typing import Any, List, Dict, Protocol
from jira_tools.services.http import get_json

class JiraClientProtocol(Protocol):
    def get_issue_data(self, issue_key: str) -> Dict[str, Any]: ...
    def get_attachments(self, issue_key: str) -> List[Dict[str,Any]]: ...
    def get_nth_attachment(self, n: int, issue_key: str) -> Dict[str,Any]: ...
    # def get_comments(self, issue_key: str): ...
    # def delete_comment(self): ...

class JiraClient(JiraClientProtocol):
    def get_issue_data(self, issue_key: str) -> Dict[str, Any]:
        """
        Fetches data attached to a Jira issue (i.e. a Robot Record)
        Args:
            issue_key (str): The unique identifier for the Jira issue.
        Returns:
            dict: The Jira issue data parsed as a JSON object.
        """
        issue_url = f"{issue_key}"
        return get_json(issue_url)

    def get_attachments(self, issue_key: str) -> List[Dict[str, Any]]:
        data = self.get_issue_data(issue_key)
        attachments = (data.get("fields", {}).get("attachment")) or []
        if not attachments:
            raise ValueError("No attachments found.")
        return attachments

    def get_nth_attachment(self, n: int, issue_key: str) -> Dict[str, Any]:
        attachments = self.get_attachments(issue_key)
        attachment_id = attachments[n]["id"]
        # Hop up one level from issue/ to attachment/ content endpoint
        attachment_url = f"../attachment/content/{attachment_id}" 
        return get_json(attachment_url, headers={}, timeout=30)
