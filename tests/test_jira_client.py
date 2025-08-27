import os, pytest, requests
from typing import Dict

from dataclasses import dataclass
from jira_tools.config.config import Config
from jira_tools.jira_client import JiraClient
from jira_tools.utils.adf import parse_adf_description
from jira_tools.services.events import get_event_history_for 
from jira_tools.services.robot_lookup import lookup_robot_pid 

@dataclass(frozen=True)    # `frozen` flag -> immutable dataclass 
class JiraTestData:
    ok_issue: str 
    bad_issue: str
    mrr_key: str
    mrouting_key: str
    rin: str
    robot_pid: str
    test_payload: Dict[str, str]

@pytest.fixture(scope="session")
def jira_test_data():
    # pull from env if provided; otherwise use defaults for safe CI
    ok_issue=os.getenv("JIRA_OK_ISSUE", "POPS-2575")
    bad_issue=os.getenv("JIRA_BAD_ISSUE", "POPS-9999")
    mrr_key=os.getenv("MASTER_ROBOT_ISSUE_KEY", "POPS-2632")
    mrouting_key=os.getenv("MASTER_ROUTING_ISSUE_KEY", "POPS-2633")
    rin=os.getenv("TEST_RIN", "BC033W000667DJ")
    robot_pid=os.getenv("TEST_ROBOT_PID", "JAG-0666")

    test_payload = { "rin": rin }

    return JiraTestData(
        ok_issue=ok_issue,
        bad_issue=bad_issue,
        mrr_key=mrr_key,
        mrouting_key=mrouting_key,
        rin=rin, 
        robot_pid=robot_pid,
        test_payload=test_payload,
    )

@pytest.fixture
def client(run_integration, jira_test_data):
    """
    Fixture for running integration tests with live Jira API calls
    """
    # skip all tests that use this fixture
    if not run_integration:
        pytest.skip("set RUN_INTEGRATION=1 to run integration_client fixture")
    # pull credentials from env/keyring via provider chain; no prompting by default
    test_config = Config.from_providers(allow_prompt=False) 
    test_config.master_robot_issue_key = jira_test_data.mrr_key
    test_config.master_routing_issue_key = jira_test_data.mrouting_key
    return JiraClient(config=test_config)

# mark test as an integration test
# integration tests are not run by default (see `conftest.py`)
@pytest.mark.integration 
def test_get_robot_record(jira_test_data, client):
    try:
        robot_record = client.get_issue_data(jira_test_data.bad_issue); # <--- non-existent issue key; should return 404
    except requests.exceptions.HTTPError as e:
        assert e.response is not None, "Expected response in HTTPError, got None"
        assert e.response.status_code == 404
    robot_record = client.get_issue_data(jira_test_data.ok_issue); # <--- known good issue key
    fields = robot_record["fields"]
    assignee = fields["assignee"]["displayName"] if fields["assignee"] else "Unassigned"
    description = parse_adf_description(robot_record)
    assert description == "Here is line #1 of the description\nHere is line #2 of the description"
    assert assignee == "Antonio Redekop"
    assert fields["summary"] == "Jaeger Test Ticket - Do Not Use"
    assert fields["status"]["name"] == "In Progress"
    assert fields["created"] == "2025-07-22T16:44:08.222-0700"

def test_get_first_json_attachment(jira_test_data, client):
    assert(client.get_nth_attachment(0, client.config.master_robot_issue_key)[jira_test_data.rin]
        == jira_test_data.robot_pid)

def test_lookup_robot(jira_test_data, client):
    assert(lookup_robot_pid(jira_test_data.test_payload, client) == jira_test_data.robot_pid)

def test_get_event_history_for(jira_test_data, client):
    assert(get_event_history_for(jira_test_data.ok_issue, client)[0].get("eventType") == "OPERATION_COMPLETE")

def test_comments(jira_test_data, client):
    # Test `add_comment`
    comment_text1 = "testComment1"
    comment_text2 = "testComment2"
    client.add_comment(jira_test_data.ok_issue, comment_text1) 
    client.add_comment(jira_test_data.ok_issue, comment_text2) 
    comments = client.get_comments(jira_test_data.ok_issue)
    assert comments[1].get("text") == "testComment1"
    assert comments[2].get("text") == "testComment2"

    # Test `delete_last_comment`
    client.delete_last_comment(jira_test_data.ok_issue)
    client.delete_last_comment(jira_test_data.ok_issue)
