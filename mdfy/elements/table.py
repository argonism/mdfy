from dataclasses import dataclass
from typing import Any, Dict, Optional, Union, Iterable, Tuple

from ._base import MdElement


@dataclass
class TableData:
    """Data model for markdown table content.

    Attributes:
        header (list[str]): Column headers of the table
        row_labels (list[str]): Row labels (used when table is transposed)
        values (list[list[Any]]): 2D array of table values
    """

    header: list[str]
    row_labels: list[str]
    values: Iterable[Union[list[Any], Tuple]]

    @classmethod
    def from_dict_list(
        cls,
        data: list[Dict[str, Any]],
        header: Optional[list[str]] = None,
        row_labels: Optional[list[str]] = None,
    ) -> "TableData":
        """Create TableData from a list of dictionaries.

        Args:
            data (list[dict[str, Any]]): List of dictionaries to convert to table data
            header (Optional[list[str]], optional): Custom header labels. Defaults to None.
            row_labels (Optional[list[str]], optional): Custom row labels. Defaults to None.

        Returns:
            TableData: Converted table data
        """
        if not data:
            return cls(header=[], row_labels=[], values=[])

        # Get header from data if not provided
        if header is None:
            header = list(data[0].keys())

        # Extract values using the header order
        values = []
        for row in data:
            row_values = []
            for key in data[0].keys():  # Use original keys to maintain order
                value = row.get(key, "")
                row_values.append(value)
            values.append(row_values)

        # Use provided row_labels or empty list
        row_labels = row_labels or []

        return cls(header=header, row_labels=row_labels, values=values)

    def transpose(self) -> "TableData":
        """Create a transposed version of the table data.

        Returns:
            TableData: Transposed table data
        """
        if not self.values:
            return TableData(header=[], row_labels=[], values=[])

        # Get original keys and values
        transposed_values = list(zip(*self.values))  # We only have one row in this case

        return TableData(
            header=self.row_labels
            or [""] * len(transposed_values[0]),  # First key-value pair becomes header
            row_labels=self.header,
            values=transposed_values,
        )


class MdTable(MdElement):
    """Converter for dict or list to markdown table.

    Args:
        data (dict or list): The data to convert.
        header (list[str], optional): Custom header labels. If not provided, dictionary keys will be used.
        row_labels (list[str], optional): Custom row labels. If not provided, no row labels will be shown.
        transpose (bool, optional): If True, transpose the table. Defaults to False.
        precision (Optional[int]): Number of decimal places for floats. If None, values are not formatted.

    Examples:
        >>> data = {
        ...     "Name": "John Doe",
        ...     "Age": 30,
        ...     "Occupation": "Software Engineer",
        ... }
        >>> table = MdTable(data)
        >>> print(table)
        | Name | Age | Occupation |
        | --- | --- | --- |
        | John Doe | 30 | Software Engineer |
        >>> # Custom headers
        >>> table = MdTable(data, header=["Full Name", "Years", "Job"])
        >>> print(table)
        | Full Name | Years | Job |
        | --- | --- | --- |
        | John Doe | 30 | Software Engineer |
        >>> # With row labels
        >>> data = [
        ...     {"Name": "John Doe", "Age": 30},
        ...     {"Name": "Jane Doe", "Age": 25}
        ... ]
        >>> table = MdTable(data, row_labels=["Person 1", "Person 2"])
        >>> print(table)
        | | Name | Age |
        | --- | --- | --- |
        | Person 1 | John Doe | 30 |
        | Person 2 | Jane Doe | 25 |
        >>> # Transposed table
        >>> print(MdTable(data, transpose=True))
        | | | |
        | --- | --- | --- |
        | Name | John Doe | Jane Doe |
        | Age | 30 | 25 |
    """

    def __init__(
        self,
        data: Union[Dict[str, Any], list[Dict[str, Any]]],
        header: Optional[list[str]] = None,
        row_labels: Optional[list[str]] = None,
        transpose: bool = False,
        precision: Union[None, int] = None,
    ):
        """Initialize a MdTable instance.

        Args:
            data (Union[Dict[str, Any], list[Dict[str, Any]]]): The data to convert.
            header (list[str], optional): Custom header labels. If not provided, dictionary keys will be used.
            row_labels (list[str], optional): Custom row labels. If not provided, no row labels will be shown.
            transpose (bool, optional): If True, transpose the table. Defaults to False.
            precision (Optional[int]): Number of decimal places for floats. If None, values are not formatted.
        """
        if isinstance(data, dict):
            data = [data]
        elif not isinstance(data, list):
            raise ValueError(
                "Provided data is not a dictionary or list of dictionaries"
            )

        self.data = self._flatten_data(data)
        self.header = header
        self.row_labels = row_labels
        self.transpose = transpose
        self.precision = precision

    def _flatten_data(self, data: list[Dict[str, Any]]) -> list[Dict[str, Any]]:
        """Flatten nested dictionaries in the data.

        Args:
            data (list[Dict[str, Any]]): The data to flatten.

        Returns:
            list[Dict[str, Any]]: Flattened data
        """
        flattened_data = []
        for entry in data:
            flattened_data.append(self._flatten_dict(entry))
        return flattened_data

    def _flatten_dict(
        self, d: Dict, parent_key: str = "", sep: str = "."
    ) -> Dict[str, Any]:
        """Recursively flatten a nested dictionary.

        Args:
            d (Dict): Dictionary to flatten.
            parent_key (str, optional): Key from parent dictionary. Defaults to ''.
            sep (str, optional): Separator to use between keys. Defaults to '.'.

        Returns:
            Dict: Flattened dictionary.
        """
        items = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(self._flatten_dict(v, new_key, sep=sep))
            else:
                items[new_key] = v
        return items

    def _value_to_string(self, value: Any) -> str:
        """Convert the given value to a string. If it's a floating point number,
        it will be formatted according to the precision attribute.

        Args:
            value (Any): The value to be converted.

        Returns:
            str: The string representation of the value.
        """
        if isinstance(value, float) and self.precision is not None:
            return f"{value:.{self.precision}f}"
        return str(value)

    def _build_markdown_table(self, table_data: TableData) -> str:
        """Build markdown table from TableData.

        Args:
            table_data (TableData): The table data to convert to markdown

        Returns:
            str: Markdown formatted table
        """
        if not table_data.values:
            return ""

        has_row_labels = bool(table_data.row_labels)
        num_columns = len(next(iter(table_data.values)))

        # Build header row
        header_parts = []
        if has_row_labels:
            # Empty cell for row label column
            header_parts.append("")

        if table_data.header:
            header_parts.extend(table_data.header)

        # Format header row with correct spacing
        header_cells = []
        for part in header_parts:
            if part:
                header_cells.append(f" {part} ")
            else:
                # Single space for empty cells
                header_cells.append(" ")
        header_row = "|" + "|".join(header_cells) + "|" if header_parts else None

        # Build separator row
        if has_row_labels:
            num_columns += 1
        separator_row = "|" + "|".join([" --- "] * num_columns) + "|"

        # Build value rows
        value_rows = []
        for i, row in enumerate(table_data.values):
            row_parts = []
            if has_row_labels and i < len(table_data.row_labels):
                row_parts.append(table_data.row_labels[i])
            row_parts.extend(self._value_to_string(val) for val in row)
            value_rows.append("| " + " | ".join(row_parts) + " |")

        # Combine all parts
        table_parts = []
        if header_row:
            table_parts.append(header_row)
        table_parts.append(separator_row)
        table_parts.extend(value_rows)

        return "\n".join(table_parts)

    def _to_md_table(self) -> str:
        """Convert the data to a Markdown formatted table.

        Args:
            transpose (bool, optional): If True, transpose the table. Defaults to False.
            precision (Union[None, int], optional): The precision for floating point numbers.

        Returns:
            str: Markdown formatted table.
        """
        if not self.data:
            return ""

        # Create table data
        table_data = TableData.from_dict_list(
            self.data, header=self.header, row_labels=self.row_labels
        )

        # Handle transposition
        if self.transpose:
            table_data = table_data.transpose()

        # Build markdown table
        md_table = self._build_markdown_table(table_data)

        return md_table

    def __str__(self) -> str:
        return self._to_md_table()
