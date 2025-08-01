import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
JIRA_EMAIL = os.getenv("JIRA_EMAIL") 
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN") 
JIRA_DOMAIN = os.getenv("JIRA_DOMAIN")
JIRA_URL = f"https://{JIRA_DOMAIN}/rest/api/3/issue/"

def get_robot_issue(issue_key):
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    url = f"{JIRA_URL}{issue_key}"
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch issue {issue_key}: {response.status_code} - {response.text}")
    # return the response as a Python dict
    return response.json()

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
