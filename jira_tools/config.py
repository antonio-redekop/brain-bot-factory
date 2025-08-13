import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load environment variables for local/dev usage only
# In prod, API token storage will be in a scoped variable, taken from user input
# In prod, Third-party PWM will be used for management of tokens
load_dotenv()

# Configuration
JIRA_EMAIL = os.environ["JIRA_EMAIL"]
JIRA_API_TOKEN = os.environ["JIRA_API_TOKEN"]
JIRA_DOMAIN = os.environ["JIRA_DOMAIN"]
JIRA_BASE_URL = f"https://{JIRA_DOMAIN}/rest/api/3/issue/"
AUTH = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

DEFAULT_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}
