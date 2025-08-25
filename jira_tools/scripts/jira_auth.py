"""
Usage:
  jira-auth login   # prompt & save to keyring
  jira-auth clear   # remove from keyring
  jira-auth status  # show which provider would be used
"""

import argparse
from jira_tools.config.config import Config
from jira_tools.config.credentials import (
    clear_credentials,
    EnvProvider,
    KeyringProvider,
)

def main() -> None:
    parser = argparse.ArgumentParser(prog="jira-auth")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("login")
    sub.add_parser("clear")
    sub.add_parser("status")
    args = parser.parse_args()

    if args.cmd == "login":
        Config.from_providers(allow_prompt=True)
        print("✅ Saved credentials to system keyring.")
    elif args.cmd == "clear":
        ok = clear_credentials()
        print("🗑️  Cleared." if ok else "Nothing to clear (missing env/email/domain or no entry).")
    elif args.cmd == "status":
        try:
            creds = None
            provider_name = None
            for name, provider in (
                ("Environment variables", EnvProvider()),
                ("System keyring", KeyringProvider()),
            ):
                creds = provider.load()
                if creds:
                    provider_name = name
                    break

            if provider_name:
                print(f"✅ Credentials available via {provider_name} for {creds.email} @ {creds.domain}")
            else:
                print("❌ No credentials found. Run `jira-auth login` to enter and save them.")
        except Exception as e:
            print(f"Status check error: {e}")
