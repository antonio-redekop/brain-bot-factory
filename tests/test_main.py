from app.main import get_robot_issue

def test_get_robot_issue():
    try:
        robot_issue = get_robot_issue("POPS-2575");  # <--- known good issue key
        #robot_issue = get_robot_issue("POPS-9999"); # <--- non-existent issue key
    except RuntimeError as e:
        print(f"Failed to get robot issue: {e}")
        raise

    fields = robot_issue["fields"]
    assignee = fields["assignee"]["displayName"] if fields["assignee"] else "Unassigned"
    description = fields["description"]["content"][0]["content"][0]["text"]
    # extract a list of comments
    comments = [
        c["body"]["content"][0]["content"][0]["text"] for c in fields["comment"]["comments"]
    ]

    assert description == "Here is the description"
    assert assignee == "Antonio Redekop"
    assert fields["summary"] == "Jaeger Test Ticket - Do Not Use"
    assert fields["status"]["name"] == "In Progress"
    assert fields["created"] == "2025-07-22T16:44:08.222-0700"
    assert comments[0] == "Test Comment #1"
