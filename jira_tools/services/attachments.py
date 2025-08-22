from jira_tools.services.http import get_json
from jira_tools.jira_api_client import JiraClient
# from jira_tools.services.issues import get_robot_record

def get_first_json_attachment(issue_key: str, client: JiraClient) -> dict:
    """
    Reads the contents of a single JSON attachment attached to a Jira issue.
    Returns the parsed JSON of the first attachment.
    """
    data = client.get_issue_data(issue_key)
    attachments = (data.get("fields", {}).get("attachment")) or []
    if not attachments:
        raise ValueError("No attachments found.")

    attachment_id = attachments[0]["id"]
    # Hop up one level from issue/ to attachment/ content endpoint
    return get_json(f"../attachment/content/{attachment_id}", headers={}, timeout=30)
