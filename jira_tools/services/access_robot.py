from typing import Dict

from jira_tools.services.attachments import get_first_json_attachment

def lookup_robot(payload: Dict[str, str], *, mrr_issue_key: str) -> str:
    """
    Given a QR payload like {"rin": "BC033W000008NH"}, return the robotId (e.g., "JAG-0007")
    by reading the first JSON attachment from the Master Robot Record (Jira issue).
    `master_robot_record.json` format is a flat map: { RIN -> robotId }.
    """
    rin = (payload or {}).get("rin")
    if not rin:
        raise ValueError("QR payload must include 'rin'.")

    # Load the attachment JSON from the Master Robot Record issue
    mrr_json = get_first_json_attachment(mrr_issue_key)
    if not isinstance(mrr_json, dict) or not mrr_json:
        raise ValueError("Master Robot Record attachment must be a non-empty JSON object (RIN -> robotId).")
    try:
        return str(mrr_json[rin])
    except KeyError as e:
        raise ValueError(f"RIN '{rin}' not found in Master Robot Record.") from e
