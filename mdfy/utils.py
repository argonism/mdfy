"""Utility functions for mdfy package."""

from typing import List, Iterable
from urllib.parse import quote

from mdfy.types import ContentElementType, ContentType, MdElement


def flattern(content: ContentType) -> List[ContentElementType]:
    """Flattens an iterable of elements.

    Args:
        content (Iterable): The iterable of elements to flatten.

    Returns:
        List: The flattened list of elements.
    """

    if not isinstance(content, Iterable):
        return [content]

    result: list[ContentElementType] = []
    for item in content:
        if isinstance(item, MdElement) or isinstance(item, str):
            result.append(item)
        else:
            result.extend(flattern(item))
    return result


def generate_anchor(text: str) -> str:
    """Generates an anchor from header text.

    Args:
        text (str): The header text.

    Returns:
        str: The anchor text.
    """
    return quote(text.lower().replace(" ", "-"))
