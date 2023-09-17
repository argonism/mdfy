from ._base import MdElement


class MdHeader(MdElement):
    def __init__(self, content: str, level: int = 1):
        """
        Initializes an instance of the MdHeader class to represent a Markdown header.

        Args:
            content (str): The content of the header.
            level (int, optional): The header level. Defaults to 1.
        """
        self.content = content
        self.level = level

    def __str__(self) -> str:
        """
        Returns a string representation of the header in Markdown format.

        Returns:
            str: String representation of the header.
        """
        return "#" * self.level + " " + self.content
