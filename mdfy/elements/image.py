import logging

from ._base import MdElement

logger = logging.getLogger(__name__)


class MdImage(MdElement):
    """Represents a Markdown image.

    Attributes:
        src (str): The source URL or path of the image.
        alt (str): The alternative text for the image.

    Examples:
        >>> from mdfy.elements import MdImage
        >>>
        >>> image = MdImage("https://example.com/image.png")
        >>> print(image)
        ![](https://example.com/image.png)
        >>>
        >>> image = MdImage("https://example.com/image.png", alt="Example image")
        >>> print(image)
        ![Example image](https://example.com/image.png)
    """

    def __init__(self, src: str, alt: str = "") -> None:
        """Initializes an instance of the MdImage class to represent a Markdown image.

        Args:
            src (str): The source URL or path of the image.
            alt (str, optional): The alternative text for the image. Defaults to an empty string.
        """
        self.src = src
        self.alt = alt

    def __str__(self) -> str:
        """Returns a string representation of the image in Markdown format.

        Returns:
            str: String representation of the image.

        Warnings:
            If the image source is None, it will log a warning and set the source to an empty string.
        """
        src = self.src
        if src is None:
            logger.warning("Image source is None, setting to empty string")
            src = ""
        return f"![{self.alt}]({src})"
