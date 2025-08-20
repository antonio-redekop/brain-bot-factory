from __future__ import annotations
from flask import Blueprint, request, jsonify, current_app

robots_bp = Blueprint("robots", __name__, url_prefix="/v1/robots")

@robots_bp.post("/resolve")
def resolve_robot():
    """
    Body: { "rin": "<RIN string>" }
    Response: { "robotPid": "<production id>" }
    """
    payload = request.get_json(silent=True) or {}
    rin = payload.get("rin")
    if not isinstance(rin, str) or not rin.strip():
        return jsonify({"error": "BadRequest", "detail": "rin (string) is required"}), 400

    # Next step: wire to helper, e.g.:
    # from jira_tools.services.access_robot import lookup_robot
    # robot_pid = lookup_robot({"rin": rin}, mrr_issue_key=current_app.config["MASTER_ROBOT_ISSUE_KEY"])
    # return jsonify({"robotPid": robot_pid})

    return jsonify({"error": "NotImplemented", "detail": "resolve_robot not wired yet"}), 501

@robots_bp.get("/<issueKey>/events")
def robot_events(issueKey: str):
    """
    Path: /v1/robots/<issueKey>/events
    Response: [ { eventType, operationNumber, operationName, operationStatus, operator,
                  timestamp, robotStatus, productionStatus, operatorComment } ... ]
    (All fields present; use None for not-applicable; operatorComment last)
    """

    # Next step: wire to helper, e.g.:
    # from jira_tools.services.access_robot import build_robot_history
    # events = build_robot_history(issueKey)
    # return jsonify(events)

    return jsonify({"error": "NotImplemented", "detail": "robot_events not wired yet"}), 501
