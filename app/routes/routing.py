from __future__ import annotations
from flask import Blueprint, jsonify, current_app

# flask blueprints are used to organize routes and logic
# url prefix ensures all routes in the blueprint are grouped under base URL
routing_bp = Blueprint("routing", __name__, url_prefix="/v1")

@routing_bp.get("/routing/<robotPid>")
def get_routing(robotPid: str):
    """
    Path: /v1/routing/<robotPid>
    Response: routing record JSON (selected by highest semver covering effectivity)
    """

    # from jira_tools.services.access_robot import fetch_routing
    # record = fetch_routing(robotPid, mroute_issue_key=current_app.config["MASTER_ROUTING_ISSUE_KEY"])
    # return jsonify(record)

    return jsonify({"error": "NotImplemented", "detail": "get_routing not wired yet"}), 501
