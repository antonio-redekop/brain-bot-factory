from __future__ import annotations
from typing import Any, Dict, List, Optional

from jira_tools.http import get_json, post_json, delete as http_delete
from jira_tools.adf import build_adf_comment_body, parse_adf_comment

def get_comments(issue_key: str) -> List[Dict[str, Any]]:
    """
    Gets all comments from an existing Jira issue
    Args:
        issue_key (str): The unique key of the Jira issue (e.g., "PROJ-123").
    Returns:
        List of all comments
    """
    # Fetch all comments
    comments_url = f"{issue_key}/comment"
    response = get_json(comments_url)

    # Gets comments, if key is available, else returns empty list
    comments = response.get("comments", [])
    if not comments:
        print(f"No comments found for issue {issue_key}.")
    parsed_comments = [parse_adf_comment(c) for c in comments]

    return parsed_comments

def add_comment(issue_key: str, comment_text: str = "This is a default comment.") -> Dict[str, Any]:
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

    return post_json(comment_url, payload)

def delete_last_comment(issue_key: str) -> None:
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
    comments = get_comments(issue_key)
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
    http_delete(delete_url)
    print(f"Deleted comment ID {comment_id} from issue {issue_key}.")
