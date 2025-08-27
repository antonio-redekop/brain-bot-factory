# brain-bot-factory 

## Authorization

To enable the `jira-auth` command, activate virtual env and install in editable mode.

1) `source .venv/bin/activate`
2) `pip install -e .`

## Usage

**Login**
- Prompt for Jira credentials and save them securely in your system keyring:
    - `jira-auth login`

**Status**
- Check whether credentials are available:
   - `jira-auth status`

**Clear**
- Remove stored credentials from the system keyring:
    - `jira-auth clear`

## Testing

- Run integration tests only
`pytest -m integration`

- Run all other tests except those marked "integration"
`pytest -m "not integration`   # run everything except tests marked "integration"
