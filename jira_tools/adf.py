from __future__ import annotations
from typing import Any, Dict, List, Optional

def build_adf_comment_body(text: str) -> Dict[str, Any]:
    """
    Construct an ADF-formatted JSON payload for a Jira comment.
    """
    return {
        "body": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": text}],
                }
            ],
        }
    }

def adf_to_text(doc: Optional[Dict[str, Any]]) -> str:
    """
    Convert a Jira/Atlassian ADF document into plain text.

    Minimal but resilient:
      - Supports 'doc' -> paragraphs with text nodes
      - Supports 'hardBreak' as newline
      - Ignores unrecognized node types without crashing
    """
    if not isinstance(doc, dict) or doc.get("type") != "doc":
        return ""

    lines: List[str] = []

    def text_from_node(node: Dict[str, Any]) -> str:
        t = node.get("type")
        if t == "text":
            return node.get("text", "")
        if t == "hardBreak":
            return "\n"
        # Generic container: flatten children
        buf = []
        for child in node.get("content", []) or []:
            buf.append(text_from_node(child))
        s = "".join(buf)
        # Treat block-ish nodes as line-producing
        if t in {"paragraph", "heading"}:
            if not s.endswith("\n"):
                s += "\n"
        return s

    for block in doc.get("content", []) or []:
        lines.append(text_from_node(block))

    out = "".join(lines)

    # Normalize: collapse triple newlines, trim edges
    while "\n\n\n" in out:
        out = out.replace("\n\n\n", "\n\n")
    return out.strip()

def parse_adf_comment(comment: Dict[str, Any]) -> Dict[str, Any]:
    """
    Parse a Jira comment object and extract key metadata using adf_to_text().
    """
    body = comment.get("body", {})
    return {
        "id": comment.get("id"),
        "text": adf_to_text(body),
        "author_name": comment.get("author", {}).get("displayName"),
        "author_email": comment.get("author", {}).get("emailAddress"),
        "created": comment.get("created"),
        "updated": comment.get("updated"),
        "public": comment.get("jsdPublic"),
        "url": comment.get("self"),
    }

def parse_adf_description(robot_record: Dict[str, Any]) -> str:
    """
    Extract plain text from an issue's description field (ADF) using adf_to_text().
    """
    desc = (robot_record.get("fields") or {}).get("description")
    return adf_to_text(desc)
