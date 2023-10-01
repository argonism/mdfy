from pathlib import Path
from typing import List, Union

from .elements import MdElement


def write(content: str, filepath: str) -> None:
    with open(filepath, "w") as file:
        for item in content:
            file.write(str(item) + "\n")


class Mdfier:
    """Writes Markdown content to a file.

    Attributes:
        filepath (Path): The path to the file.
    """

    def __init__(self, filepath: Union[str, Path]) -> None:
        """Initializes an instance of the Mdfier class to write Markdown content to a file.

        Args:
            filepath (Union[str, Path]): The path to the file.
        """

        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)

    @classmethod
    def stringify(cls, contents: List[Union[str, MdElement]]) -> str:
        """Converts the given Markdown content to a string.

        Args:
            content (Union[str, MdElement]): The Markdown content to convert to a string.
        """

        return "\n".join([str(item) for item in contents])

    def write(self, contents: List[Union[str, MdElement]]) -> None:
        """Writes the given Markdown content to the file.

        Args:
            content (Union[str, MdElement]): The Markdown content to write to the file.
        """

        markdown = self.stringify(contents)
        with open(self.filepath, "w") as file:
            file.write(markdown + "\n")
