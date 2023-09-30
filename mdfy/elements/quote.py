from ._base import MdElement


class MdQuote(MdElement):
    def __init__(self, content):
        """
        Initializes an instance of the MdQuote class to represent a Markdown blockquote.

        Args:
            content (str or MdElement): The content of the quote.
        """
        self.content = content

    def __str__(self) -> str:
        """
        Returns a string representation of the blockquote in Markdown format.

        Returns:
            str: String representation of the blockquote.
        """
        # Convert the content to string if it's an instance of MdElement
        content_str = (
            str(self.content) if isinstance(self.content, MdElement) else self.content
        )
        content_str = "" if content_str is None else content_str

        # Ensure content is not None
        lines = [""] if len(content_str) <= 0 else content_str.splitlines()

        # Create a blockquote by prefixing each line with '>'
        return "\n".join([f"> {line}" for line in lines])
