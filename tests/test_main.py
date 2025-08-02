import requests

from app.main import get_robot_issue
from app.main import extract_description
from app.main import add_comment
from app.main import delete_last_comment

def test_get_robot_issue():
    try:
        robot_issue = get_robot_issue("POPS-9999"); # <--- non-existent issue key; should return 404
    except requests.exceptions.HTTPError as e:
        if e.response.status_code != 404:
            raise
    try:
        robot_issue = get_robot_issue("POPS-2575"); # <--- known good issue key
    except requests.exceptions.HTTPError as e:
        print(f"Failed to get robot issue: {e}")
        raise
    fields = robot_issue["fields"]
    assignee = fields["assignee"]["displayName"] if fields["assignee"] else "Unassigned"
    description = extract_description(fields["description"])

    assert description == "Here is line #1 of the description\nHere is line #2 of the description"
    assert assignee == "Antonio Redekop"
    assert fields["summary"] == "Jaeger Test Ticket - Do Not Use"
    assert fields["status"]["name"] == "In Progress"
    assert fields["created"] == "2025-07-22T16:44:08.222-0700"

# def test_add_comment():
#     add_comment("POPS-2575")
#
# def test_delete_last_comment():
#     delete_last_comment("POPS-2575")

def test_comment():
    # Test `add_comment`
    comment_text1 = "testComment1"
    comment_text2 = "testComment2"
    add_comment("POPS-2575", comment_text1) 
    add_comment("POPS-2575", comment_text2) 

    # Get robot issue
    try:
        robot_issue = get_robot_issue("POPS-2575"); # <--- known good issue key
    except requests.exceptions.HTTPError as e:
        print(f"Failed to get robot issue: {e}")
        raise
    fields = robot_issue["fields"]

    # Extract a list of comments
    comments = [
        c["body"]["content"][0]["content"][0]["text"] for c in fields["comment"]["comments"]
    ]
    assert comments[0] == "testComment1"
    assert comments[1] == "testComment2"

    # Test `delete_last_comment`
    delete_last_comment("POPS-2575")
    delete_last_comment("POPS-2575")
