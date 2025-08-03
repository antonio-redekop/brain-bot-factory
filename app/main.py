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
AUTH = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

def jira_request(method, endpoint, json_payload=None):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    url = f"{JIRA_URL}{endpoint}"

    # requests.request always returns response object; does not raise exceptions
    response = requests.request(method, url, headers=headers, json=json_payload, auth=AUTH)
    try:
        # `raise_for_status` preserves response object, unlike manually raising
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # HTTPError does not auto include the response object; must attach manually
        # `from e` preserves the original error object, since we are re-raising
        raise requests.exceptions.HTTPError(
            f"Jira API {method} request failed: {response.status_code} - {response.text}",
            response = response,
        ) from e
    return response

def get_robot_issue(issue_key):
    """
    Fetches a Jira issue using the provided issue key.
    Args:
        issue_key (str): The unique identifier for the Jira issue.
    Returns:
        dict: The Jira issue data parsed as a JSON object.
    """
    issue_url = f"{issue_key}"
    response = jira_request("GET", issue_url)
    return response.json()

def get_comments(issue_key):
    """
    Gets all comments from an existing Jira issue
    Args:
        issue_key (str): The unique key of the Jira issue (e.g., "PROJ-123").
    Returns:
        List of all comments
    """
    robot_data = get_robot_issue(issue_key)
    
    # Fetch all comments
    comments_url = f"{issue_key}/comment"
    response = jira_request("GET", comments_url)
    
    # Gets comments, if key is available, else returns empty list
    comments = response.json().get("comments", [])
    if not comments:
        print(f"No comments found for issue {issue_key}.")
    parsed_comments = [parse_jira_comment(c) for c in comments] 

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
    response = jira_request("POST", comment_url, payload)
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
    # comments_url = f"{JIRA_URL}{issue_key}/comment"
    url = f"{issue_key}/comment"

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
    delete_url = f"{url}/{comment_id}"
    jira_request("DELETE", delete_url) 
    print(f"Deleted comment ID {comment_id} from issue {issue_key}.")

def parse_jira_comment(comment):
    """
    Parses Jira comment object and extracts key metadata.
    Args:
        comment (dict): A Jira comment object in ADF format.
    Returns:
        dict: extracted metadata 
    """
    # Extract the plain text from the ADF content
    def extract_text(adf_body):
        if adf_body.get("type") != "doc":
            return ""
        lines = []
        for block in adf_body.get("content", []):
            if block.get("type") == "paragraph":
                text = ""
                for inner in block.get("content", []):
                    if inner.get("type") == "text":
                        text += inner.get("text", "")
                lines.append(text)
        return "\n".join(lines).strip()

    return {
        "id": comment.get("id"),
        "text": extract_text(comment.get("body", {})),
        "author_name": comment.get("author", {}).get("displayName"),
        "author_email": comment.get("author", {}).get("emailAddress"),
        "created": comment.get("created"),
        "updated": comment.get("updated"),
        "public": comment.get("jsdPublic"),
        "url": comment.get("self"),
    }

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
