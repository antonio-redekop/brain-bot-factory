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

    #Raise an error for any status code that isn't 2xx
    response.raise_for_status()

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
