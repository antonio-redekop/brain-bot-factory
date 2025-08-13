from jira_tools.http import get_json, post_json, delete
from jira_tools.adf import build_adf_comment_body, parse_adf_comment

def get_robot_record(issue_key):
    """
    Fetches a Robot Record (Jira issue) using the provided issue key.
    Args:
        issue_key (str): The unique identifier for the Jira issue.
    Returns:
        dict: The Jira issue data parsed as a JSON object.
    """
    issue_url = f"{issue_key}"
    response = get_json(issue_url)
    return response

def get_comments(issue_key):
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

def add_comment(issue_key, comment_text="This is a default comment."):
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

    response = post_json(comment_url, payload)
    return response

def delete_last_comment(issue_key):
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
    delete(delete_url)
    print(f"Deleted comment ID {comment_id} from issue {issue_key}.")

def read_attachment(issue_key: str) -> dict:
    """
    Reads the contents of a single JSON attachment attached to a Jira issue.
    Returns the parsed JSON of the first attachment.
    """
    data = get_robot_record(issue_key)
    attachments = (data.get("fields", {}).get("attachment")) or []
    if not attachments:
        raise ValueError("No attachments found.")

    attachment_id = attachments[0]["id"]
    # Hop up one level from issue/ to attachment/ content endpoint
    return get_json(f"../attachment/content/{attachment_id}", headers={}, timeout=30)
