"""Type definitions for mdfy package."""

from typing import Union, Iterable

from .elements import MdElement

ContentElementType = Union[str, MdElement]
_ContentType = Union[ContentElementType, Iterable[ContentElementType]]
ContentType = Union[_ContentType, Iterable[_ContentType]]
