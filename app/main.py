import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os
import json

from jira_tools.http import get_json
from jira_tools.http import post_json
from jira_tools.http import delete

MASTER_ROUTING_RECORD_KEY = "POPS-2633"

def get_robot_record(issue_key):
    """
    Fetches a Robot Record (Jira issue) using the provided issue key.
    Args:
        issue_key (str): The unique identifier for the Jira issue.
    Returns:
        dict: The Jira issue data parsed as a JSON object.
    """
    issue_url = f"{issue_key}"
    response = get_json(issue_url)
    return response

def get_comments(issue_key):
    """
    Gets all comments from an existing Jira issue
    Args:
        issue_key (str): The unique key of the Jira issue (e.g., "PROJ-123").
    Returns:
        List of all comments
    """
    
    # Fetch all comments
    comments_url = f"{issue_key}/comment"
    response = get_json(comments_url)
    
    # Gets comments, if key is available, else returns empty list
    comments = response.get("comments", [])
    if not comments:
        print(f"No comments found for issue {issue_key}.")
    parsed_comments = [parse_jira_comment(c) for c in comments] 

    return parsed_comments

def add_comment(issue_key, comment_text="This is a default comment."):
    """
    Posts a comment to an existing Jira issue.
    Args:
        issue_key (str): The unique key of the Jira issue (e.g., "PROJ-123").
        comment_text (str): The text of the comment to post.
    Returns:
        dict: The JSON response from Jira with comment details.
    """
    comment_url = f"{issue_key}/comment"
    
    # payload must be ADF formated JSON
    payload = build_adf_comment_body(comment_text)

    response = post_json(comment_url, payload)
    return response

def delete_last_comment(issue_key):
    """
    Deletes the most recent comment from a Jira issue.
    Note: Authenticated user must have delete permissions in Jira
    Args:
        issue_key (str): The Jira issue key.
    Raises:
        RuntimeError: If fetching or deleting the comment fails.
    """
    comments_url = f"{issue_key}/comment"

    # Get comments
    comments = get_comments(issue_key)
    if not comments:
        return

    # Identify most recent comment
    # `max` avoids sorting; is more performant
    # both apply `key` callable to each item of iterable prior to evaluation 
    # last_comment = sorted(comments, key=lambda c: c["created"])[-1]
    last_comment = max(comments, key=lambda c: c["created"])
    comment_id = last_comment["id"]

    # Delete most recent comment
    delete_url = f"{comments_url}/{comment_id}"
    delete(delete_url)
    print(f"Deleted comment ID {comment_id} from issue {issue_key}.")

def parse_jira_comment(comment):
    """
    Parses Jira comment object and extracts key metadata.
    Args:
        comment (dict): A Jira comment object in ADF format.
    Returns:
        dict: extracted metadata 
    """
    # Extract the plain text from the ADF content
    def extract_text(adf_body):
        if adf_body.get("type") != "doc":
            return ""
        lines = []
        for block in adf_body.get("content", []):
            if block.get("type") == "paragraph":
                text = ""
                for inner in block.get("content", []):
                    if inner.get("type") == "text":
                        text += inner.get("text", "")
                lines.append(text)
        return "\n".join(lines).strip()

    return {
        "id": comment.get("id"),
        "text": extract_text(comment.get("body", {})),
        "author_name": comment.get("author", {}).get("displayName"),
        "author_email": comment.get("author", {}).get("emailAddress"),
        "created": comment.get("created"),
        "updated": comment.get("updated"),
        "public": comment.get("jsdPublic"),
        "url": comment.get("self"),
    }

def extract_description(robot_record):
    """
    Extract and concatenate plain text from a Jira description field within a robot record.
    The description field uses Atlassian Document Format (ADF), a nested JSON structure.
    Args:
        robot_record: ADF representation of a Jira issue
    Returns:
        str: Complete plain-text representation of the description, with blocks separated by newlines.
    """
    # description_field (dict): JSON structure of the description field from Jira issue (robot_record)
    description_field = robot_record["fields"]["description"]
    description_text = ""
    for block in description_field["content"]:
        if "content" in block:
            for inner_block in block["content"]:
                if inner_block.get("type") == "text":
                    description_text += inner_block.get("text", "") + "\n"
    return description_text.strip()

def build_adf_comment_body(text):
    """Constructs an ADF-formatted JSON payload for a Jira comment."""
    return {
        "body": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": text}]
                }
            ]
        }
    }

def read_attachment(issue_key: str) -> dict:
    """
    Reads the contents of a single JSON attachment attached to a Jira issue.
    Returns the parsed JSON of the first attachment.
    """
    data = get_robot_record(issue_key)
    attachments = (data.get("fields", {}).get("attachment")) or []
    if not attachments:
        raise ValueError("No attachments found.")

    attachment_id = attachments[0]["id"]
    # Hop up one level from issue/ to attachment/ content endpoint
    return get_json(f"../attachment/content/{attachment_id}", headers={}, timeout=30)
