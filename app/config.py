from __future__ import annotations
import os

class Config:
    # where master attachments live (Jira issue keys)
    # os.environ raises a KeyError exception if environmental variable is not found
    MASTER_ROBOT_ISSUE_KEY = os.environ["JIRA_MASTER_ROBOT_ISSUE_KEY"]
    MASTER_ROUTING_ISSUE_KEY = os.environ["JIRA_MASTER_ROUTING_ISSUE_KEY"]
    # Basic Flask settings
    JSON_SORT_KEYS = False  # preserve insertion order (keep operatorComment last, etc.)
