import logging

logger = logging.getLogger(__name__)


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


class MdControlElement(MdElement):
    """Represents a control element in Markdown.


    This element is used to control the rendering of the markdown content.
    It should not be stringified.
    """

    def __str__(self) -> str:
        logger.warning("Control elements should not be stringified.")
        return super().__str__()
