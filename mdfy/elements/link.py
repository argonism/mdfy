import warnings
from typing import Optional

from ._base import MdElement


class MdLink(MdElement):
    """Represents a Markdown link.

    Attributes:
        url (str): The URL of the link.
        text (str): The display text for the link.
        title (str): The title attribute for the link.

    Examples:
        >>> from mdfy.elements import MdLink
        >>>
        >>> link = MdLink("https://www.example.com", "example")
        >>> print(link)
        [example](https://www.example.com)
        >>>
        >>> link = MdLink("https://www.example.com", "example", title="example")
        >>> print(link)
        [example](https://www.example.com "example")
    """

    def __init__(self, url: str, text: str = "", title: Optional[str] = None) -> None:
        """Initializes an instance of the MdLink class to represent a Markdown link.

        Args:
            url (str): The URL of the link.
            text (str, optional): The display text for the link. Defaults to an empty string.
            title (str, optional): The title attribute for the link. Defaults to None.
        """
        self.url = url
        self.text = text
        self.title = title

    def __str__(self) -> str:
        """Returns a string representation of the link in Markdown format.

        Returns:
            str: String representation of the link.

        Warnings:
            If the link URL is None, it will log a warning and set the URL to an empty string.
        """
        url = self.url
        if url is None:
            warnings.warn("Link URL is None, setting to empty string")
            url = ""
        text_str = f"{self.text}" if self.text else url
        title_str = f' "{self.title}"' if self.title else ""
        return f"[{text_str}]({url}{title_str})"
