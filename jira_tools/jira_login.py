from jira_tools.config.config import Config

# One-time interactive setup to store token in keyring
if __name__ == "__main__":
    Config.from_providers(allow_prompt=True)
    print("✅Credentials saved to system keychain.")
