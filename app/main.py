import requests
from requests.auth import HTTPBasicAuth

from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
JIRA_EMAIL = os.getenv("JIRA_EMAIL") 
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN") 
JIRA_DOMAIN = os.getenv("JIRA_DOMAIN")

def get_jira_issue():
    issue_key = "POPS-2575"

    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

    url = f"https://{JIRA_DOMAIN}/rest/api/3/issue/{issue_key}"
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, auth=auth)
    # print(response.json())
    return response.status_code
