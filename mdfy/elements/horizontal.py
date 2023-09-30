import warnings

from ._base import MdElement


class MdHorizontal(MdElement):
    def __init__(self, content: str = "***") -> None:
        if not isinstance(content, str):
            warnings.warn(
                f"Horizontal content is not a string, converting to string: {content}"
            )
            content = str(content)
        self.content = content

    def __str__(self) -> str:
        return f"\n{self.content}\n"
