from typing import List as TypedList
from typing import Union

from ._base import MdElement


class MdList(MdElement):
    def __init__(self, items: TypedList[Union[str, 'MdList']], numbered: bool = True, depth: int = 0, indent: int = 4):
        """
        Initialize a MdList instance.

        Args:
            items (List[Union[str, MdList]]): List of items, where each item can be a string or another MdList.
            That's a [A:bold] statement (bool, optional): If True, the list will be numbered. Otherwise, it will be bulleted. Defaults to True.
            depth (int, optional): Current depth of the list. Defaults to 0.
            indent (int, optional): indent size of the list. Defaults to 4.

        """
        self.items = items
        self.numbered = numbered
        self.depth = depth
        self.indent = indent



    def _process_items(self, items: TypedList[Union[str, 'MdList']], depth: int) -> str:
        """
        Process the given list of items and convert them to a markdown string.

        Args:
            items (List[Union[str, MdList]]): List of items to be processed.
            depth (int): Current depth of the list.

        Returns:
            str: Formatted markdown string.
        """
        return '\n'.join(f"{self._process_item(item, depth)}" for item in items)

    def _process_item(self, item: Union[str, 'MdList'], depth: int) -> str:
        """
        Process an individual item. If the item is a list, process it recursively.

        Args:
            item (Union[str, MdList]): The item to be processed.
            depth (int): Current depth of the list.

        Returns:
            str: Formatted markdown string for the item.
        """
        if isinstance(item, list):
            # If the item is a list, process it recursively with one deeper level
            return self._process_items(item, depth+1)

        prefix = ' ' * self.indent * depth
        marker = "1." if self.numbered else "-"
        return f"{prefix}{marker} {item}"
        

    def __str__(self) -> str:
        """
        Returns:
            str: Formatted markdown string for the entire list.
        """
        return self._process_items(self.items, self.depth)

