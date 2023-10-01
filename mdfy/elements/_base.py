class MdElement:
    """Represents a Markdown element.

    Attributes:
        content (str or MdElement): The content of the element.
    """

    def __str__(self) -> str:
        raise NotImplementedError

    def to_str(self) -> str:
        """Returns a string representation of the element in Markdown format.

        Returns:
            str: String representation of the element.
        """

        return str(self)
