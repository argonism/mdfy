import warnings

from ._base import MdElement


class MdHorizontal(MdElement):
    """Represents a Markdown horizontal rule.

    Attributes:
        content (str): The content for representing the horizontal rule.

    Examples:
        >>> from mdfy.elements import MdHorizontal
        >>>
        >>> horizontal = MdHorizontal()
        >>> print(horizontal)
        ***
        >>>
        >>> horizontal = MdHorizontal("---")
        >>> print(horizontal)
        ---
    """

    def __init__(self, content: str = "***") -> None:
        """Initializes an instance of the MdHorizontal class to represent a Markdown horizontal rule.

        Args:
            content (str, optional): The content of the horizontal rule. Defaults to "***".
        """
        if not isinstance(content, str):
            warnings.warn(
                f"Horizontal content is not a string, converting to string: {content}"
            )
            content = str(content)
        self.content = content

    def __str__(self) -> str:
        return f"\n{self.content}\n"
