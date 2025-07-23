from app.main import get_jira_issue

def test_hello():
    assert get_jira_issue() == 200
