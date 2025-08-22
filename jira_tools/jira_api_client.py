from typing import Any, List, Dict, Protocol
from jira_tools.services.http import get_json, post_json, delete as http_delete
from jira_tools.utils.adf import build_adf_comment_body, parse_adf_comment
from jira_tools.config.config import Config

class JiraClientProtocol(Protocol):
    def get_issue_data(self, issue_key: str) -> Dict[str, Any]: ...
    def get_attachments(self, issue_key: str) -> List[Dict[str,Any]]: ...
    def get_nth_attachment(self, n: int, issue_key: str) -> Dict[str,Any]: ...
    def get_comments(self, issue_key: str) -> List[Dict[str, Any]]: ...
    def add_comment(self, issue_key: str, comment_text: str) -> Dict[str, Any]: ...
    def delete_last_comment(self, issue_key: str) -> None: ...

class JiraClient(JiraClientProtocol):
    def __init__(self, config: Config | None = None):
        self.config = config or Config()

    def get_issue_data(self, issue_key: str) -> Dict[str, Any]:
        """
        Fetches data attached to a Jira issue (i.e. a Robot Record)
        Args:
            issue_key (str): The unique identifier for the Jira issue.
        Returns:
            dict: The Jira issue data parsed as a JSON object.
        """
        issue_url = f"{issue_key}"
        return get_json(issue_url, self)

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
        return get_json(attachment_url, self, headers={}, timeout=30)

    def get_comments(self, issue_key: str) -> List[Dict[str, Any]]:
        """
        Gets all comments from an existing Jira issue
        Args:
            issue_key (str): The unique key of the Jira issue (e.g., "PROJ-123").
        Returns:
            List of all comments
        """
        # Fetch all comments
        comments_url = f"{issue_key}/comment"
        response = get_json(comments_url, self)

        # Gets comments, if key is available, else returns empty list
        comments = response.get("comments", [])
        if not comments:
            print(f"No comments found for issue {issue_key}.")
        parsed_comments = [parse_adf_comment(c) for c in comments]

        return parsed_comments

    def add_comment(self, issue_key: str, comment_text: str = "This is a default comment.") -> Dict[str, Any]:
        """
        Posts a comment to an existing Jira issue.
        Args:
            issue_key (str): The unique key of the Jira issue (e.g., "PROJ-123").
            comment_text (str): The text of the comment to post.
        Returns:
            dict: The JSON response from Jira with comment details.
        """
        comment_url = f"{issue_key}/comment"

        # payload must be ADF formated JSON
        payload = build_adf_comment_body(comment_text)

        return post_json(comment_url, payload, self)

    def delete_last_comment(self, issue_key: str) -> None:
        """
        Deletes the most recent comment from a Jira issue.
        Note: Authenticated user must have delete permissions in Jira
        Args:
            issue_key (str): The Jira issue key.
        Raises:
            RuntimeError: If fetching or deleting the comment fails.
        """
        comments_url = f"{issue_key}/comment"

        # Get comments
        comments = self.get_comments(issue_key)
        if not comments:
            return

        # Identify most recent comment
        # `max` avoids sorting; is more performant
        # both apply `key` callable to each item of iterable prior to evaluation
        # last_comment = sorted(comments, key=lambda c: c["created"])[-1]
        last_comment = max(comments, key=lambda c: c["created"])
        comment_id = last_comment["id"]

        # Delete most recent comment
        delete_url = f"{comments_url}/{comment_id}"
        http_delete(delete_url, self)
        print(f"Deleted comment ID {comment_id} from issue {issue_key}.")
