import abc


class MdFormatter(abc.ABC):
    """Abstract base class for Markdown formatters."""

    @abc.abstractmethod
    def format(self, text: str) -> str:
        """Formats the text and returns the formatted text.

        Args:
            text (str): The text to be formatted.

        Returns:
            str: The formatted text.
        """
        raise NotImplementedError
