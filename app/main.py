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
