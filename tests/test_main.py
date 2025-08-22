import pytest, requests
from jira_tools.jira_api_client import JiraClient
from jira_tools.services.adf import parse_adf_description
from jira_tools.services.access_robot import lookup_robot, build_robot_history

JIRA_TEST_ISSUE = "POPS-2575"
JIRA_TEST_ISSUE_BAD = "POPS-9999"
JIRA_MASTER_ROBOT_RECORD = "POPS-2632"
JIRA_MASTER_ROUTING_RECORD = "POPS-2633"

TEST_RIN = "BC033W000667DJ"    # maps to JAG-0666 in MRR
TEST_ROBOT_PID = "JAG-0666"
QR_TEST_PAYLOAD = { "rin": TEST_RIN }

@pytest.fixture
def client():
    return JiraClient()

def test_get_robot_record(client):
    try:
        robot_record = client.get_issue_data(JIRA_TEST_ISSUE_BAD); # <--- non-existent issue key; should return 404
    except requests.exceptions.HTTPError as e:
        assert e.response is not None, "Expected response in HTTPError, got None"
        assert e.response.status_code == 404
    robot_record = client.get_issue_data(JIRA_TEST_ISSUE); # <--- known good issue key
    fields = robot_record["fields"]
    assignee = fields["assignee"]["displayName"] if fields["assignee"] else "Unassigned"
    description = parse_adf_description(robot_record)
    assert description == "Here is line #1 of the description\nHere is line #2 of the description"
    assert assignee == "Antonio Redekop"
    assert fields["summary"] == "Jaeger Test Ticket - Do Not Use"
    assert fields["status"]["name"] == "In Progress"
    assert fields["created"] == "2025-07-22T16:44:08.222-0700"

def test_get_first_json_attachment(client):
    assert(client.get_nth_attachment(0, JIRA_MASTER_ROBOT_RECORD)[TEST_RIN] == TEST_ROBOT_PID)

def test_lookup_robot(client):
    assert(lookup_robot(
        QR_TEST_PAYLOAD,
        client,
        mrr_issue_key = JIRA_MASTER_ROBOT_RECORD
    ) == TEST_ROBOT_PID)

def test_build_robot_history(client):
    assert(build_robot_history(JIRA_TEST_ISSUE, client)[0].get("eventType") == "OPERATION_COMPLETE")

def test_comments(client):
    # Test `add_comment`
    comment_text1 = "testComment1"
    comment_text2 = "testComment2"
    client.add_comment(JIRA_TEST_ISSUE, comment_text1) 
    client.add_comment(JIRA_TEST_ISSUE, comment_text2) 
    comments = client.get_comments(JIRA_TEST_ISSUE)
    assert comments[1].get("text") == "testComment1"
    assert comments[2].get("text") == "testComment2"

    # Test `delete_last_comment`
    client.delete_last_comment(JIRA_TEST_ISSUE)
    client.delete_last_comment(JIRA_TEST_ISSUE)
