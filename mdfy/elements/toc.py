from typing import Union, Optional

from mdfy.types import MdWritableItem
from mdfy.utils import generate_anchor
from mdfy.elements._base import MdControlElement
from mdfy.elements.header import MdHeader


class MdTableOfContents(MdControlElement):
    """Represents a table of contents in Markdown.

    This element can generate a table of contents from a list of markdown elements.
    If contents are provided during initialization, it will generate the table of contents
    when stringified. Otherwise, it will return just the title.

    Attributes:
        title (str): The title of the table of contents.
        level (int): The heading level for the table of contents title.
        contents (Optional[ContentType]): The markdown contents to generate TOC from.
    """

    def __init__(
        self,
        contents: Union[list[MdWritableItem], None] = None,
        render_all: bool = False,
    ) -> None:
        """Initializes a table of contents element.

        Args:
            title (str): The title of the table of contents.
            level (int): The heading level for the table of contents title.
        """
        super().__init__()

        self._contents = contents
        self._render_all = render_all

    def render(
        self,
        contents: Union[list[MdWritableItem], None] = None,
        index: Optional[int] = None,
    ) -> str:
        """Generates a table of contents from a list of elements.

        Args:
            elements (list[ContentElementType]): The list of elements to generate TOC from.
            toc (MdTableOfContents): The table of contents element with configuration.

        Returns:
            str: The generated table of contents.
        """
        contents_to_render = self._contents or contents

        if contents_to_render is None:
            raise ValueError(
                "No contents provided. "
                "Either contents argument or _contents attribute must be provided."
            )

        if len(contents_to_render) == 0:
            return ""
        if index is not None:
            if index >= len(contents_to_render):
                return ""
            contents_to_render = contents_to_render[index:]

        headers = [elem for elem in contents_to_render if isinstance(elem, MdHeader)]

        lines = []
        for header in headers:
            indent = "  " * (header.level - 1)
            anchor = generate_anchor(header.content)
            lines.append(f"{indent}- [{header.content}](#{anchor})")

        return "\n".join(lines) + "\n"
