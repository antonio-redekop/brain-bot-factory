from typing import Dict
from jira_tools.jira_api_client import JiraClient

def lookup_robot_pid(payload: Dict[str, str], client: JiraClient) -> str:
    """
    Given a QR payload containing the RIN, looks in the master robot record to find the matching robot_pid
    Master robot record is a flat map: { RIN -> robot_pid }.
    Arguments:
        payload: Dict[str, str]   QR payload
        client: JiraClient
    Returns
        robot_pid: str
    """
    rin = (payload or {}).get("rin")
    if not rin:
        raise ValueError("QR payload must include 'rin'.")
    # Get Master Robot Record (json) attachment from the Master Robot Issue
    mrr_json = client.get_nth_attachment(0, client.config.master_robot_issue_key)
    if not isinstance(mrr_json, dict) or not mrr_json:
        raise ValueError("Master Robot Record attachment must be a non-empty JSON object (RIN -> robotPid).")
    try:
    # Return robot_pid, if found
        return str(mrr_json[rin])
    except KeyError as e:
        raise ValueError(f"RIN '{rin}' not found in Master Robot Record.") from e
