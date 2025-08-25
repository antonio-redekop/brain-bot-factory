import re
from typing import Any, Dict, List, Tuple
from jira_tools.jira_client import JiraClient
from jira_tools.utils.parse import parse_robot_pid, parse_semver

# matches a start-end effectivity range e.g. 0001-0086
_EFFECTIVITY_RE = re.compile(r"^(?P<start>\d{4})-(?P<end>\d{4})$")

def get_master_routing(client: JiraClient) -> List[Dict[str, Any]]:
    mrouting_issue_key = client.config.master_routing_issue_key
    attachment = client.get_nth_attachment(0, mrouting_issue_key)
    master_routing = (attachment or {}).get("masterRoutingRecord")
    if not isinstance(master_routing, list) or not master_routing:
        raise ValueError("Master Routing Record attachment must contain non-empty 'masterRoutingRecord' array.")
    return master_routing

def get_routing_for(robot_pid: str, master_routing: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Given a robot_pid and the master routing list, we return the correct production routing
    Highest semantic version wins among effectivity matches
    Arguments:
        robot_pid: str                          e.g. JAG-0007
        master_routing: List[Dict[str, Any]]
    Returns:
        A dict of the applicable routing with highest semantic version
    """
    # Create list to hold applicable routing candidates; we sort list later
    candidates: List[Tuple[Tuple[int, int, int], Dict[str, Any]]] = []

    # Get the numeric portion from `robot_pid`
    seq = parse_robot_pid(robot_pid)

    # Iterate through routing versions contained in master routing
    # Append all applicable candidates with matching effectivity
    # a - starting effectivity
    # b - ending effectivity
    for routing in master_routing:
        eff = routing.get("effectivity", "")
        m = _EFFECTIVITY_RE.match(eff)
        if not m:
            continue
        a, b = int(m.group("start")), int(m.group("end"))
        if a <= seq <= b:
            ver = str(routing.get("version", "0.0.0"))
            candidates.append((parse_semver(ver), routing))

    if not candidates:
        raise LookupError(f"No routing found that covers robot '{robot_pid}'.")

    # Sort the candidates to get the highest semantic version
    candidates.sort(key=lambda t: t[0], reverse=True)
    # Return highest semantic version of routing applicable to the robot_pid
    return candidates[0][1]
