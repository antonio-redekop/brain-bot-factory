from __future__ import annotations
from typing import Any, Dict

from jira_tools.http import get_json

def get_robot_record(issue_key: str) -> Dict[str, Any]:
    """
    Fetches a Robot Record (Jira issue) using the provided issue key.
    Args:
        issue_key (str): The unique identifier for the Jira issue.
    Returns:
        dict: The Jira issue data parsed as a JSON object.
    """
    issue_url = f"{issue_key}"
    return get_json(issue_url)
