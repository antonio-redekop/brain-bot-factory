import requests
from typing import Any, Mapping, Optional
from jira_tools import config

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
) -> requests.Response:
    """
    Perform an HTTP request to the Jira API.
    Raises:
        JiraHttpError: If Jira responds with a 4xx/5xx status code.
    """
    merged_headers = {**config.DEFAULT_HEADERS, **(headers or {})}
    url = f"{config.JIRA_BASE_URL}{endpoint}" 

    # requests.request always returns response object; does not raise exceptions
    resp = requests.request(
        method,
        url,
        headers=merged_headers,
        json=json_payload,
        auth=config.AUTH,
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

def get_json(endpoint: str, **kwargs):
    """Perform a GET request and return parsed JSON."""
    return jira_request("GET", endpoint, **kwargs).json()

def post_json(endpoint: str, payload, **kwargs):
    """Perform a POST request and return parsed JSON."""
    return jira_request("POST", endpoint, json_payload=payload, **kwargs).json()

def delete(endpoint: str, **kwargs):
    """Perform a DELETE request."""
    jira_request("DELETE", endpoint, **kwargs)
