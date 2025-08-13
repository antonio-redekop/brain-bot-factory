from jira_tools.http import get_json 

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
