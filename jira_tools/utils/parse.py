import re
from typing import Tuple

# matches semantic version numbers e.g. 0.1.0
_SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")

def parse_semver(v: str) -> Tuple[int, int, int]:
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

def parse_robot_pid(robot_pid: str) -> int:
    """
    Given a robot_pid, e.g. JAG-0007, returns the numeric portion e.g. 0007
    """
    # re.search looks anywhere in the string for a match
    # But in this case, we anchor to the end of the string
    m = re.search(r"(\d{4})$", robot_pid)
    if not m:
        raise ValueError(f"robotPid '{robot_pid}' must end with 4 digits (e.g., JAG-0007).")
    return int(m.group(1))
