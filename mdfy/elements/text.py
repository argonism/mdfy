import re

from ._base import MdElement


class MdText(MdElement):
    STYLE_PATTERNS = {
        'strong': '***{}***',
        'bold': '**{}**',
        'italic': '*{}*',
        'not': '~~{}~~',
        'underline': '<u>{}</u>',
    }

    def __init__(self, content: str):
        """
        Initialize a MdText instance.

        Args:
            content (str): The content string containing potential style markers.
        """
        self.content = content

    def __str__(self) -> str:
        """
        Returns the styled content as per the specified style markers.

        Returns:
            str: Formatted markdown string with the appropriate styles applied.
        """
        result = self.content

        for style, pattern in self.STYLE_PATTERNS.items():
            # re.subを使ってマッチした部分を変換します
            result = re.sub(r"\[(.*?):" + style + r"\]", lambda m: pattern.format(m.group(1)), result)

        return result

    def __add__(self, other: 'MdText') -> 'MdText':
        """
        Adds two MdText objects together.

        Args:
            other (MdText): The other MdText object to be added.

        Returns:
            MdText: A new MdText object containing the concatenated content of the two objects.
        """
        return MdText(str(self) + str(other))
