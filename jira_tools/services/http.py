from __future__ import annotations
import requests
from typing import TYPE_CHECKING, Any, Mapping, Optional

if TYPE_CHECKING:  # Only evaluated by type checkers, not at runtime
    from jira_tools.jira_client import JiraClient

class JiraHttpError(requests.exceptions.HTTPError):
    """Raised when Jira API returns an error response."""
    pass

def jira_request(
    method: str,
    endpoint: str,
    json_payload: Optional[Any] = None,
    *,    # <---- positional only separator
    headers: Optional[Mapping[str, str]] = None,
    timeout: float = 30.0,
    client: JiraClient,
) -> requests.Response:
    """
    Perform an HTTP request to the Jira API.
    Raises:
        JiraHttpError: If Jira responds with a 4xx/5xx status code.
    """
    merged_headers = {**client.config.default_headers, **(headers or {})}
    url = f"{client.config.base_url}{endpoint}" 

    # requests.request always returns response object; does not raise exceptions
    resp = requests.request(
        method,
        url,
        headers=merged_headers,
        json=json_payload,
        auth=client.config.auth,
        timeout=timeout)
    try:
        # `raise_for_status` preserves response object, unlike manually raising
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # re-raise with the response attached
        # HTTPError does not auto include the response object; must attach manually
        # `from e` preserves the original error object, since we are re-raising
        raise JiraHttpError(
            f"Jira API {method} request failed: {resp.status_code} - {resp.text}",
            response=resp,
        ) from e
    return resp

def get_json(endpoint: str, client: JiraClient, **kwargs):
    """Perform a GET request and return parsed JSON."""
    return jira_request("GET", endpoint, client=client, **kwargs).json()

def post_json(endpoint: str, payload, client: JiraClient, **kwargs):
    """Perform a POST request and return parsed JSON."""
    return jira_request("POST", endpoint, json_payload=payload, client=client, **kwargs).json()

def delete(endpoint: str, client:JiraClient, **kwargs):
    """Perform a DELETE request."""
    jira_request("DELETE", endpoint, client=client, **kwargs)
