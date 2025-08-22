import os
from dotenv import load_dotenv
from dataclasses import dataclass
from requests.auth import HTTPBasicAuth

# Load environment variables for local/dev usage only
# In prod, API token storage will be in a scoped variable, taken from user input
# In prod, Third-party PWM will be used for management of tokens
load_dotenv()

@dataclass
class Config:
    jira_email: str = os.environ["JIRA_EMAIL"]
    jira_api_token: str = os.environ["JIRA_API_TOKEN"]
    jira_domain = os.environ["JIRA_DOMAIN"]
    master_robot_issue_key = os.environ["JIRA_MASTER_ROBOT_ISSUE_KEY"]
    master_routing_issue_key = os.environ["JIRA_MASTER_ROUTING_ISSUE_KEY"]

    @property
    def base_url(self) -> str:
        return f"https://{self.jira_domain}/rest/api/3/issue/"

    @property
    def auth(self) -> HTTPBasicAuth:
        return HTTPBasicAuth(self.jira_email, self.jira_api_token)

    @property
    def default_headers(self) -> dict:
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
