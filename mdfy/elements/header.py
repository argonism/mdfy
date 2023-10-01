from ._base import MdElement


class MdHeader(MdElement):
    """Represents a Markdown header.

    Attributes:
        content (str): The content of the header.
        level (int): The header level.

    Examples:
        >>> from mdfy.elements import MdHeader
        >>>
        >>> header = MdHeader("This is a header")
        >>> print(header)
        # This is a header
        >>>
        >>> header = MdHeader("This is a header", level=2)
        >>> print(header)
        ## This is a header
    """

    def __init__(self, content: str, level: int = 1) -> None:
        """Initializes an instance of the MdHeader class to represent a Markdown header.

        Args:
            content (str): The content of the header.
            level (int, optional): The header level. Defaults to 1.
        """
        self.content = content
        self.level = level

    def __str__(self) -> str:
        """Returns a string representation of the header in Markdown format.

        Returns:
            str: String representation of the header.
        """
        return "#" * self.level + " " + self.content
