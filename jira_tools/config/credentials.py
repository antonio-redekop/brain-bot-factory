from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Protocol
import os
import getpass

try:
    import keyring 
except Exception:
    keyring = None  # allow running without keyring installed

# appears in OS keyring app
SERVICE_NAME = "jira_tools"

@dataclass
class Credentials:
    email: str
    api_token: str
    domain: str

class CredentialProvider(Protocol):
    def load(self) -> Optional[Credentials]: ...
    def save(self, creds: Credentials) -> None: ...

def _scope_key(domain: str, email: str) -> str:
    return f"jira:{domain}:{email}"

class EnvProvider:
    """Reads from process env; does not save back."""
    def load(self) -> Optional[Credentials]:
        email = os.getenv("JIRA_EMAIL")
        token = os.getenv("JIRA_API_TOKEN")
        domain = os.getenv("JIRA_DOMAIN")
        if email and token and domain:
            return Credentials(email=email, api_token=token, domain=domain)
        return None

    # we don't write to env in code
    # def save(self, creds: Credentials) -> None:
    #     return

class KeyringProvider:
    """Stores token in OS keychain, keyed by (domain, email)."""
    def load(self) -> Optional[Credentials]:
        if keyring is None:
            return None
        email = os.getenv("JIRA_EMAIL")
        domain = os.getenv("JIRA_DOMAIN")
        if not (email and domain):
            return None
        key = _scope_key(domain, email)
        token = keyring.get_password(SERVICE_NAME, key)
        if token:
            return Credentials(email=email, api_token=token, domain=domain)
        return None

    def save(self, creds: Credentials) -> None:
        if keyring is None:
            return
        key = _scope_key(creds.domain, creds.email)
        keyring.set_password(SERVICE_NAME, key, creds.api_token)

class PromptProvider:
    """
    Interactively prompt for any missing credentials.
    Servers/CI won't use this at runtime; instead run a 'login' command once.
    """
    def load(self) -> Optional[Credentials]:
        email = os.getenv("JIRA_EMAIL") or input("Jira email: ").strip()
        domain = os.getenv("JIRA_DOMAIN") or input("Jira domain (e.g. myco.atlassian.net): ").strip()
        token = getpass.getpass("Jira API token (input hidden): ").strip()
        if email and token and domain:
            return Credentials(email=email, api_token=token, domain=domain)
        return None

    def save(self, creds: Credentials) -> None:
        if keyring is not None:
            KeyringProvider().save(creds)

def load_credentials(allow_prompt: bool = False) -> Credentials:
    """
    Resolution order:
      1) Explicit env (dev/CI)
      2) Keyring (prod runtime)
      3) Prompt (optional; use in 'login' command, not servers)
    """
    for provider in (EnvProvider(), KeyringProvider()):
        creds = provider.load()
        if creds:
            return creds

    if allow_prompt:
        creds = PromptProvider().load()
        if creds:
            PromptProvider().save(creds)
            return creds

    raise RuntimeError(
        "No Jira credentials found. "
        "Set env vars (JIRA_EMAIL, JIRA_API_TOKEN, JIRA_DOMAIN), "
        "or run the interactive login (see CLI below), "
        "or ensure keyring has a token saved."
    )
