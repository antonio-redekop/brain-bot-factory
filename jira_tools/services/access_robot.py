import re
from typing import Dict, Tuple, List, Any
from jira_tools.jira_api_client import JiraClient

# matches semantic version numbers e.g. 0.1.0
_SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
# matches a start-end effectivity range e.g. 0001-0086
_EFFECTIVITY_RE = re.compile(r"^(?P<start>\d{4})-(?P<end>\d{4})$")
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

def _get_semver(v: str) -> Tuple[int, int, int]:
    """
    Input is a semantic version string e.g. "0.1.0"
    Validates string against a regex 
    Returns a tuple containing MAJOR, MINOR, PATCH 
    """
    # match looks for matches starting at position 0 of the string
    # Will return None, if entire string does not match
    m = _SEMVER_RE.match(v or "")
    if not m:
        return (0, 0, 0)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)))

def _get_robot_seq(robot_pid: str) -> int:
    """
    Given a robot_pid, e.g. JAG-0007, returns the numeric portion e.g. 0007
    """
    # re.search looks anywhere in the string for a match
    # But in this case, we anchor to the end of the string
    m = re.search(r"(\d{4})$", robot_pid)
    if not m:
        raise ValueError(f"robotPid '{robot_pid}' must end with 4 digits (e.g., JAG-0007).")
    return int(m.group(1))

def fetch_routing(robot_pid: str, client: JiraClient, *, mroute_issue_key: str) -> Dict[str, Any]:
    """
    Given a robot_pid, we return the correct production routing from the Master Routing Record issue
    Highest semantic version wins among effectivity matches
    Arguments:
        robot_pid: str                 e.g. JAG-0007
        mroute_issue_key: str          e.g. POPS-0666
    Returns:
        A dict of the applicable routing with highest semantic version
    """
    doc = client.get_nth_attachment(0, mroute_issue_key)
    mrr = (doc or {}).get("masterRoutingRecord")
    if not isinstance(mrr, list) or not mrr:
        raise ValueError("Master Routing Record attachment must contain non-empty 'masterRoutingRecord' array.")

    # Get the numeric portion from `robot_pid`
    seq = _get_robot_seq(robot_pid)

    # Create list to hold our routing candidates; we can sort list later
    routing_list: List[Tuple[Tuple[int, int, int], Dict[str, Any]]] = []

    # Iterate through routing versions contained in MRR and append to `routing_list`
    # a - starting effectivity
    # b - ending effectivity
    for record in mrr:
        eff = record.get("effectivity", "")
        m = _EFFECTIVITY_RE.match(eff)
        if not m:
            continue
        a, b = int(m.group("start")), int(m.group("end"))
        if a <= seq <= b:
            ver = str(record.get("version", "0.0.0"))
            routing_list.append((_get_semver(ver), record))

    if not routing_list:
        raise LookupError(f"No routing found that covers robot '{robot_pid}'.")

    routing_list.sort(key=lambda t: t[0], reverse=True)
    return routing_list[0][1]

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
