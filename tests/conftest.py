# `pytest.conf` serves as a means of providing fixtures for an entire directory
import os, pytest
from dotenv import load_dotenv

# Load environment variables for dev usage only (harmless in prod)
load_dotenv()
_RUN_INTEGRATION = os.getenv("RUN_INTEGRATION") == "1"

print(_RUN_INTEGRATION)

# defines a fixture with session scope (available to all files in directory)
@pytest.fixture(scope="session")
def run_integration():
    return _RUN_INTEGRATION
 
def pytest_runtest_setup(item):
    # skip integration tests unless explicitly enabled
    # we can mark specific tests with `@pytest.mark.<MARKER>`
    # in this case, we choose to mark integration tests with `integration` marker
    if "integration" in item.keywords and not _RUN_INTEGRATION:
        pytest.skip("set RUN_INTEGRATION=1 to run")
