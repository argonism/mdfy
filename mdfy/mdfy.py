from io import TextIOWrapper
from pathlib import Path
from types import TracebackType
from typing import List, Optional, Type, Union

from .elements import MdElement


class Mdfier:
    """Writes Markdown content to a file.

    Attributes:
        filepath (Path): The path to the file.

    Examples:
        >>> from mdfy import Mdfier
        >>> from mdfy.elements import MdHeader, MdQuote
        >>>
        >>> mdfier = Mdfier("README.md")
        >>> mdfier.write([
        ...     MdHeader("Hello, world!", 1),
        ...     MdQuote("This is a quote.")
        ... ])
        >>>
        >>> with open("README.md") as file:
        ...     print(file.read())
        ...
        # Hello, world!
        > This is a quote.
    """

    def __init__(self, filepath: Union[str, Path], encoding: str = "utf-8") -> None:
        """Initializes an instance of the Mdfier class to write Markdown content to a file.

        Args:
            filepath (Union[str, Path]): The path to the file.
        """

        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        self.file_object: Optional[TextIOWrapper] = None
        self._encoding = encoding

    def __enter__(self) -> "Mdfier":
        """Returns the Mdfier instance.

        Returns:
            Mdfier: The Mdfier instance.
        """

        self.file_object = self.filepath.open("w", encoding=self._encoding)
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Writes the Markdown content to the file.

        Args:
            exc_type (type): The type of the exception.
            exc_value (Exception): The exception that was raised.
            traceback (Traceback): The traceback of the exception.
        """
        if self.file_object is None:
            return
        self.file_object.close()

    @classmethod
    def stringify(cls, contents: List[Union[str, MdElement]]) -> str:
        """Converts the given Markdown content to a string.

        Args:
            content (Union[str, MdElement]): The Markdown content to convert to a string.
        """



        return "\n".join([str(item) for item in contents])

    def write(self, contents: Union[List[Union[str, MdElement]], MdElement]) -> None:
        """Writes the given Markdown content to the file.

        Args:
            content (Union[str, MdElement]): The Markdown content to write to the file.
        """

        if not isinstance(contents, list):
            contents = [contents]
        markdown = self.stringify(contents)
        if self.file_object is None:
            self.filepath.write_text(markdown + "\n", encoding=self._encoding)
        else:
            self.file_object.write(markdown + "\n")
