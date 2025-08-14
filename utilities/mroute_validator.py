#!/usr/bin/env python3
"""
mroute_validator.py — Strict validator for Master Routing Record (MRoute) JSON.

Usage:
  python mroute_validator_strict.py /path/to/master_routing_record.json [--robot-id JAG-0007] [--strict] [--debug]

Behavior:
 - Strict by default: schema must match exactly; no silent coercions.
 - Overlapping effectivity ranges are allowed.
 - Applicability for --robot-id is chosen by highest semantic version only (releasedAt ignored).
 - --debug prints key fields and types to help diagnose issues without relaxing validation.

Exit codes:
  0 valid, 1 invalid (schema/semantics), 2 file read error, 3 JSON parse error
"""

import re
import sys
import json
import argparse
from typing import Any, Dict, List, Tuple, Optional
from urllib.parse import urlparse

SEMVER_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
SCHEMAVER_RE = re.compile(r"^[0-9]+\.[0-9]+$")
EFFECTIVITY_RE = re.compile(r"^(?P<start>[0-9]{4})-(?P<end>[0-9]{4})$")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
ROBOT_ID_RE = re.compile(r"^[A-Za-z]+-(?P<num>[0-9]{4})$")

def _type_val(v):
    return f"({type(v).__name__}) {v!r}"

def is_http_url(s: str) -> bool:
    try:
        u = urlparse(s)
        return u.scheme in ("http", "https") and bool(u.netloc)
    except Exception:
        return False

def parse_effectivity(eff: str) -> Tuple[int, int]:
    m = EFFECTIVITY_RE.match(eff or "")
    if not m:
        raise ValueError(f"Effectivity '{eff}' must match ####-####.")
    a, b = int(m.group("start")), int(m.group("end"))
    if a > b:
        raise ValueError(f"Effectivity start {a:04d} cannot be greater than end {b:04d}.")
    return a, b

def extract_robot_seq(robot_id: str) -> int:
    m = ROBOT_ID_RE.match(robot_id or "")
    if not m:
        raise ValueError("robotId must be like PREFIX-0001")
    return int(m.group("num"))

def validate_operations(ops: List[Dict[str, Any]]) -> List[str]:
    errs: List[str] = []
    last_seq = 0
    seen_seq = set()
    for i, op in enumerate(ops, start=1):
        loc = f"operations[{i}]"
        if not isinstance(op, dict):
            errs.append(f"{loc}: must be an object; saw {_type_val(op)}")
            continue

        seq = op.get("sequence")
        if not isinstance(seq, int) or seq < 1:
            errs.append(f"{loc}.sequence: integer >= 1 required; saw {_type_val(seq)}")
        else:
            if seq in seen_seq:
                errs.append(f"{loc}.sequence: duplicate value {seq}")
            if seq <= last_seq:
                errs.append(f"{loc}.sequence: must be strictly increasing (prev {last_seq}, got {seq})")
            seen_seq.add(seq)
            last_seq = max(last_seq, seq)

        name = op.get("operationName")
        if not isinstance(name, str) or not name.strip():
            errs.append(f"{loc}.operationName: non-empty string required; saw {_type_val(name)}")

        sw = op.get("standardWork")
        if not isinstance(sw, str) or not is_http_url(sw):
            errs.append(f"{loc}.standardWork: valid http(s) URL required; saw {_type_val(sw)}")

        opid = op.get("operationId")
        if opid is not None and not isinstance(opid, str):
            errs.append(f"{loc}.operationId: if present, must be a string; saw {_type_val(opid)}")

    return errs

def validate_record(rec: Dict[str, Any], idx: int) -> List[str]:
    errs: List[str] = []
    loc = f"masterRoutingRecord[{idx}]"
    if not isinstance(rec, dict):
        return [f"{loc}: must be an object; saw {_type_val(rec)}"]

    version = rec.get("version")
    if not isinstance(version, str) or not SEMVER_RE.match(version):
        errs.append(f"{loc}.version: semantic version (X.Y.Z) required; saw {_type_val(version)}")

    eff = rec.get("effectivity")
    if not isinstance(eff, str):
        errs.append(f"{loc}.effectivity: string required; saw {_type_val(eff)}")
    else:
        try:
            parse_effectivity(eff)
        except Exception as e:
            errs.append(f"{loc}.effectivity: {e}")

    ops = rec.get("operations")
    if not isinstance(ops, list) or not ops:
        errs.append(f"{loc}.operations: non-empty array required; saw {_type_val(ops)}")
    else:
        errs.extend(validate_operations(ops))

    eco = rec.get("eco")
    if eco is not None and not isinstance(eco, str):
        errs.append(f"{loc}.eco: if present, must be a string; saw {_type_val(eco)}")

    released_at = rec.get("releasedAt")
    if released_at is not None and not isinstance(released_at, str):
        errs.append(f"{loc}.releasedAt: if present, must be a string; saw {_type_val(released_at)}")

    released_by = rec.get("releasedBy")
    if released_by is not None:
        if not isinstance(released_by, str) or not EMAIL_RE.match(released_by):
            errs.append(f"{loc}.releasedBy: valid email required; saw {_type_val(released_by)}")

    notes = rec.get("notes")
    if notes is not None and not isinstance(notes, str):
        errs.append(f"{loc}.notes: if present, must be a string; saw {_type_val(notes)}")

    return errs

def validate_top_level(doc: Dict[str, Any]) -> List[str]:
    errs: List[str] = []
    if not isinstance(doc, dict):
        return ["Top-level JSON must be an object; saw " + _type_val(doc)]

    sv = doc.get("schemaVersion")
    if not isinstance(sv, str) or not SCHEMAVER_RE.match(sv):
        errs.append("schemaVersion: string like '1.0' required; saw " + _type_val(sv))

    mrr = doc.get("masterRoutingRecord")
    if not isinstance(mrr, list) or not mrr:
        errs.append("masterRoutingRecord: non-empty array required; saw " + _type_val(mrr))

    return errs

def semver_tuple(v: str) -> Tuple[int, int, int]:
    try:
        x, y, z = (int(p) for p in v.split("."))
        return x, y, z
    except Exception:
        return (0, 0, 0)

def applicable_record(records: List[Dict[str, Any]], robot_id: str) -> Optional[Dict[str, Any]]:
    """
    Pick the applicable routing solely by highest semantic version among
    records whose effectivity covers the robotId's numeric segment.
    """
    seq = extract_robot_seq(robot_id)
    candidates = []
    for rec in records:
        eff = rec.get("effectivity", "")
        if not isinstance(eff, str) or not EFFECTIVITY_RE.match(eff):
            continue
        a, b = parse_effectivity(eff)
        if a <= seq <= b:
            ver = rec.get("version") if isinstance(rec.get("version"), str) else "0.0.0"
            candidates.append((semver_tuple(ver), rec))

    if not candidates:
        return None

    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1]

def validate_document(doc: Dict[str, Any], robot_id: str = None):
    errs = validate_top_level(doc)
    chosen = None
    mrr = doc.get("masterRoutingRecord") if isinstance(doc, dict) else None
    if isinstance(mrr, list):
        for idx, rec in enumerate(mrr):
            errs.extend(validate_record(rec, idx))

        if robot_id:
            chosen = applicable_record(mrr, robot_id)
            if not chosen:
                errs.append(f"--robot-id {robot_id}: not covered by any effectivity range")

    return errs, chosen

def show_json_parse_error(path: str, e):
    # e is a json.JSONDecodeError with lineno, colno, pos
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        i = max(0, e.lineno - 3)
        j = min(len(lines), e.lineno + 2)
        snippet = "\n".join(f"{k+1:04d} | {lines[k]}" for k in range(i, j))
        caret = " " * (e.colno + 7) + "^"
        print("ERROR: invalid JSON:", e)
        print("Context:")
        print(snippet)
        print(caret)
    except Exception:
        print("ERROR: invalid JSON:", e)

def main():
    ap = argparse.ArgumentParser(description="Validate a Master Routing Record JSON.")
    ap.add_argument("file", help="Path to master_routing_record.json")
    ap.add_argument("--strict", action="store_true", help="(kept for compatibility; validation is strict by default)")
    ap.add_argument("--robot-id", help="Select the applicable routing for this robotId (e.g., JAG-0007)")
    ap.add_argument("--debug", action="store_true", help="Print key fields/types for diagnostics")
    args = ap.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"ERROR: could not read file: {e}", file=sys.stderr)
        sys.exit(2)

    try:
        doc = json.loads(text)
    except json.JSONDecodeError as e:
        show_json_parse_error(args.file, e)
        sys.exit(3)
    except Exception as e:
        print(f"ERROR: invalid JSON: {e}")
        sys.exit(3)

    if args.debug:
        try:
            rec0 = (doc.get("masterRoutingRecord") or [])[0]
        except Exception:
            rec0 = None
        print("[DEBUG] schemaVersion:", _type_val(doc.get("schemaVersion")))
        if isinstance(rec0, dict):
            print("[DEBUG] version:", _type_val(rec0.get("version")))
            print("[DEBUG] releasedBy:", _type_val(rec0.get("releasedBy")))
        else:
            print("[DEBUG] first record missing or not an object")

    errs, chosen = validate_document(doc, robot_id=args.robot_id)
    if errs:
        print("INVALID:")
        for i, msg in enumerate(errs, start=1):
            print(f"  {i:02d}. {msg}")
        sys.exit(1)

    print("VALID ✅")
    if chosen is not None:
        eff = chosen.get("effectivity")
        ver = chosen.get("version")
        eco = chosen.get("eco", "")
        rby = chosen.get("releasedBy", "")
        print(f"APPLIES → version={ver}, effectivity={eff}, releasedBy={rby}, eco={eco}")
    sys.exit(0)

if __name__ == "__main__":
    main()
