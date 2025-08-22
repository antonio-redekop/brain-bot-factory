import re
from typing import Dict, List, Any
from jira_tools.jira_api_client import JiraClient

# Matches Markdown-style heading for an event
_EVENT_HEADER_RE = re.compile(r"^\s*#{1,6}\s*(?P<etype>[A-Z_]+)\s*$", re.MULTILINE)
# Match bullet line: "- key: value" (also allows unicode bullets/dashes)
_EVENT_FIELD_RE  = re.compile(
    r"""^\s*[-–—*•]\s*(?P<key>[A-Za-z][\w]*)\s*:\s*(?P<val>.+?)\s*$""",
    re.MULTILINE
)
# Canonical schema fields (operatorComment last)
_EVENT_ALL_FIELDS = [
    "eventType",
    "timestamp",
    "operationSeq",
    "operationName",
    "operationStatus",
    "operator",
    "productionStatus",
    "operatorComment",   # << always last
]

def lookup_robot(payload: Dict[str, str], client: JiraClient,*, mrr_issue_key: str) -> str:
    """
    Given a QR payload like {"rin": "BC033W000008NH"}, return the robotProdId (e.g., "JAG-0007")
    by reading the first JSON attachment from the Master Robot Record (Jira issue).
    `master_robot_record.json` format is a flat map: { RIN -> robotProdId }.
    """
    rin = (payload or {}).get("rin")
    if not rin:
        raise ValueError("QR payload must include 'rin'.")

    # Load the attachment JSON from the Master Robot Record issue
    mrr_json = client.get_nth_attachment(0, mrr_issue_key)
    if not isinstance(mrr_json, dict) or not mrr_json:
        raise ValueError("Master Robot Record attachment must be a non-empty JSON object (RIN -> robotPid).")
    try:
        return str(mrr_json[rin])
    except KeyError as e:
        raise ValueError(f"RIN '{rin}' not found in Master Robot Record.") from e

def build_robot_history(robot_issue_key: str, client: JiraClient) -> List[Dict[str, Any]]:
    """
    Construct robot history from the comment fields of a robot issue (robot record) 
    """
    comments = client.get_comments(robot_issue_key)  # your objects use: text, author_name, author_email, created
    events: List[Dict[str, Any]] = []

    for c in comments:
        # Use 'text' (your shape) and normalize NBSPs that Jira sometimes injects
        text = (c.get("text") or c.get("body") or "").replace("\u00A0", " ").strip()
        if not text:
            continue

        m_header = _EVENT_HEADER_RE.search(text)
        if not m_header:
            continue
        etype = m_header.group("etype").upper()

        parsed: Dict[str, Any] = {}
        for m in _EVENT_FIELD_RE.finditer(text):
            parsed[m.group("key")] = m.group("val").strip()

        # Build fixed-schema event with defaults = None
        evt: Dict[str, Any] = {f: None for f in _EVENT_ALL_FIELDS}
        evt["eventType"] = etype
        for f in _EVENT_ALL_FIELDS:
            if f in parsed:
                evt[f] = parsed[f]
        events.append(evt)

    # Sort by oldest → newest by the event's timestamp
    # Every event will have a timestamp
    events.sort(key=lambda e: e.get("timestamp") or "")
    return events
