import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

# Load environment variables from .env file in project root
# This implementation for dev only.
# In prod, API token storage will be in a scoped variable, taken from user input
# Third-party PWM will be used for management of tokens
load_dotenv()

JIRA_EMAIL = os.environ["JIRA_EMAIL"] 
JIRA_API_TOKEN = os.environ["JIRA_API_TOKEN"]
JIRA_DOMAIN = os.environ["JIRA_DOMAIN"]
JIRA_URL = f"https://{JIRA_DOMAIN}/rest/api/3/issue/"

def get_robot_issue(issue_key):
    """
    Fetches a Jira issue using the provided issue key.
    Args:
        issue_key (str): The unique identifier for the Jira issue.
    Returns:
        dict: The Jira issue data parsed as a JSON object.
    Raises:
        RuntimeError: If the request to Jira fails or returns a non-200 status code.
    """
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    url = f"{JIRA_URL}{issue_key}"
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, auth=auth)

    # Raise an error for any status code that isn't 2xx
    response.raise_for_status()

    # return the response as a Python dict
    return response.json()

def get_comments(issue_key):
    """
    Gets all comments from an existing Jira issue
    Args:
        issue_key (str): The unique key of the Jira issue (e.g., "PROJ-123").
    Returns:
        List of all comments
    Raises:
        RuntimeError: If no comments are available.
    """
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    headers = {"Accept": "application/json"}
    
    # Fetch all comments
    comments_url = f"{JIRA_URL}{issue_key}/comment"
    response = requests.get(comments_url, headers=headers, auth=auth)
    response.raise_for_status()
    
    # Gets comments, if key is available.  If not, comments is empty list. 
    comments = response.json().get("comments", [])
    if not comments:
        raise RuntimeError("No comments found on this issue.")
    return comments

def add_comment(issue_key, comment_text="This is a default comment."):
    """
    Posts a comment to an existing Jira issue.
    Args:
        issue_key (str): The unique key of the Jira issue (e.g., "PROJ-123").
        comment_text (str): The text of the comment to post.
    Returns:
        dict: The JSON response from Jira with comment details.
    Raises:
        RuntimeError: If the POST request fails.
    """
    url = f"{JIRA_URL}{issue_key}/comment"
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    # payload must be ADF formated JSON
    payload = {
        "body": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": comment_text
                        }
                    ]
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, json=payload, auth=auth)

    if not response.ok:
        raise RuntimeError(f"Failed to post comment: {response.status_code} - {response.text}")

    return response.json()

def delete_last_comment(issue_key):
    """
    Deletes the most recent comment from a Jira issue.
    Note: Authenticated user must have delete permissions in Jira
    Args:
        issue_key (str): The Jira issue key.
    Raises:
        RuntimeError: If fetching or deleting the comment fails.
    """
    comments_url = f"{JIRA_URL}{issue_key}/comment"
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    headers = {
        "Accept": "application/json",
    }

    # Get comments
    comments = []
    try:
        comments = get_comments(issue_key)
    except RuntimeError as e:
        print(f"{e}")
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
    delete_response = requests.delete(delete_url, headers=headers, auth=auth)
    
    if not delete_response.ok:
        raise RuntimeError(f"Failed to delete comment: {delete_response.status_code} - {delete_response.text}")
    
    print(f"Deleted comment ID {comment_id} from issue {issue_key}.")

def extract_description(description_field):
    """
    Extract and concatenate plain text from a Jira description field.
    The description field uses Atlassian Document Format (ADF), a nested JSON structure.
    Args:
        description_field (dict): JSON structure of the description field from Jira issue.
    Returns:
        str: Complete plain-text representation of the description, with blocks separated by newlines.
    """
    description_text = ""
    for block in description_field["content"]:
        if "content" in block:
            for inner_block in block["content"]:
                if inner_block.get("type") == "text":
                    description_text += inner_block.get("text", "") + "\n"
    return description_text.strip()
