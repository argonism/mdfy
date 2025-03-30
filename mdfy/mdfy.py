from io import TextIOWrapper
from pathlib import Path
from types import TracebackType
from typing import List, Optional, Type, Union, Iterable

from .elements import MdElement


ContentElementType = Union[str, MdElement]
_ContentType = Union[ContentElementType, Iterable[ContentElementType]]
ContentType = Union[_ContentType, Iterable[_ContentType]]


def _flattern(content: ContentType) -> List[ContentElementType]:
    """Flattens an iterable of elements.

    Args:
        content (Iterable): The iterable of elements to flatten.

    Returns:
        List: The flattened list of elements.
    """

    if not isinstance(content, Iterable):
        return [content]

    result: list[ContentElementType] = []
    for item in content:
        if isinstance(item, MdElement) or isinstance(item, str):
            result.append(item)
        else:
            result.extend(_flattern(item))
    return result


class Mdfier:
    """Writes Markdown content to a file.

    Attributes:
        filepath (Path): The path to the file.

    Examples:
        >>> from mdfy import Mdfier, MdHeader, MdQuote, MdText
        >>> # Writing Markdown content to a file
        >>> mdfier = Mdfier("quote.md")
        >>> mdfier.write([
        ...     MdHeader("Hello, world!", 1),
        ...     MdQuote("This is a quote.")
        ... ])
        >>>
        >>> with open("quote.md") as file:
        ...     print(file.read())
        ...
        # Hello, world!
        > This is a quote.

        from mdfy import MdHeader, MdQuote, MdText
        >>> mdfier = Mdfier("nest.md")
        >>> # Nested content will be flattened
        >>> mdfier.write([
        ...     MdHeader("Hello, world!", 1),
        ...     [
        ...         MdText(f"{i} * {i} = {i * i}")
        ...         for i in range(1, 3)
        ...     ]
        ... ])
        >>> with open("nest.md") as file:
        ...     print(file.read())
        ...
        # Hello, world!
        1 * 1 = 1
        2 * 2 = 4
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
    def stringify(cls, contents: ContentType, separator: str = "\n") -> str:
        """Converts the given Markdown content to a string.

        Args:
            content (Union[str, MdElement]): The Markdown content to convert to a string.
        """

        flattened_contents = _flattern(contents)
        return separator.join([str(item) for item in flattened_contents])

    def write(self, contents: ContentType) -> None:
        """Writes the given Markdown content to the file.

        Args:
            content (Union[str, MdElement]): The Markdown content to write to the file.
        """

        if not isinstance(contents, Iterable):
            contents = [contents]

        markdown = self.stringify(contents)
        if self.file_object is None:
            self.filepath.write_text(markdown + "\n", encoding=self._encoding)
        else:
            self.file_object.write(markdown + "\n")
