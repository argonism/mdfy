import re
import string
from typing import Optional

from ._base import MdElement


class MdTextFormatter(string.Formatter):
    class EchoDict(dict):
        def __missing__(self, key):
            return key

    STYLE_PATTERNS = {
        "strong": "***{}***",
        "bold": "**{}**",
        "italic": "*{}*",
        "not": "~~{}~~",
        "underline": "<u>{}</u>",
        "text": "`{}`",
    }

    def format(self, format_string, /, *args, **kwargs):
        kwargs = self.EchoDict(**kwargs)
        return self.vformat(format_string, args, kwargs)

    # STYLE_PATTERNSに基づいて、文字列を変換する
    def format_field(self, value, format_spec):
        print(value, format_spec)
        if format_spec in self.STYLE_PATTERNS:
            return self.STYLE_PATTERNS[format_spec].format(value)
        else:
            return super().format_field(value, format_spec)


class MdText(MdElement):
    def __init__(
        self, content: str, formatter: Optional[MdTextFormatter] = MdTextFormatter()
    ):
        """
        Initialize a MdText instance.

        Args:
            content (str): The content string containing potential style markers.
        """
        self.content = content
        self.formatter = formatter

    def __str__(self) -> str:
        """
        Returns the styled content as per the specified style markers.

        Returns:
            str: Formatted markdown string with the appropriate styles applied.
        """
        result = self.content
        result = self.formatter.format(result)

        return result

    def __add__(self, other: "MdText") -> "MdText":
        """
        Adds two MdText objects together.

        Args:
            other (MdText): The other MdText object to be added.

        Returns:
            MdText: A new MdText object containing the concatenated content of the two objects.
        """
        return MdText(str(self) + str(other))
