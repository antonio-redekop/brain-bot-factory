import os
from dotenv import load_dotenv
from dataclasses import dataclass
from requests.auth import HTTPBasicAuth

from jira_tools.config.credentials import load_credentials, Credentials

# Load environment variables for local/dev usage only (harmless in prod)
load_dotenv()

@dataclass
class Config:
    jira_email: str
    jira_api_token: str
    jira_domain: str
    master_robot_issue_key: str | None = None
    master_routing_issue_key: str | None = None

    @classmethod
    def from_providers(cls, allow_prompt: bool = False) -> "Config":
        creds: Credentials = load_credentials(allow_prompt=allow_prompt)
        return cls(
            jira_email=creds.email,
            jira_api_token=creds.api_token,
            jira_domain=creds.domain,
            master_robot_issue_key=os.getenv("JIRA_MASTER_ROBOT_ISSUE_KEY"),
            master_routing_issue_key=os.getenv("JIRA_MASTER_ROUTING_ISSUE_KEY"),
        )

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
