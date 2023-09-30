import logging

from ._base import MdElement

logger = logging.getLogger(__name__)


class MdCode(MdElement):
    def __init__(self, code: str, inline: bool = False, syntax: str = ""):
        """
        Initializes an instance of the MdCode class to represent Markdown code or code block.

        Args:
            code (str): The code string.
            inline (bool, optional): Determines if the code should be represented as inline or block.
                                      Defaults to block (False).
            syntax (str, optional): The programming language syntax for the code block.
                                    This only has an effect when inline is False.
        """

        if code is None:
            logger.warning("Code content is None, setting to empty string")
            code = ""

        self.code = code
        self.inline = inline
        self.syntax = syntax

        # Check for newlines to override inline setting
        if "\n" in code:
            self.inline = False

    def __str__(self) -> str:
        """
        Returns a string representation of the code in Markdown format.

        Returns:
            str: String representation of the code.

        Warnings:
            If the code is None, it will log a warning and set the code to an empty string.
        """

        code = self.code
        if self.inline:
            return f"`{code}`"
        else:
            return f"```{self.syntax}\n{code}\n```"
