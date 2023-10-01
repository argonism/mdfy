import warnings
from typing import Any, Dict, List, Optional, Union

from ._base import MdElement


class MdTable(MdElement):
    """Converter for dict or list to markdown table.

    Args:
        data (dict or list): The data to convert.
        transpose (bool, optional): If True, transpose the table. Defaults to False.
        labels (list[str], optional): Label for header when transposed. Defaults to 'Key' and 'value {i}'.
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
        >>> table = MdTable(data, transpose=True)
        >>> print(table)
        | Key | Value 0 | Value 1 | Value 2 |
        | --- | --- | --- | --- |
        | Name | John Doe |  |  |
        | Age | 30 |  |  |
        | Occupation | Software Engineer |  |  |
        >>> table = MdTable(data, transpose=True, labels=["Header", "Value"])
        >>> print(table)
        | Header | Value |
        | --- | --- |
        | Name | John Doe |
        | Age | 30 |
        | Occupation | Software Engineer |
        >>> # you can use nested dict
        >>> data = {
        ...     "Name": "John Doe",
        ...     "Age": 30,
        ...     "Occupation": "Software Engineer",
        ...     "Address": {
        ...         "Street": "123 Main St",
        ...         "City": "Anytown",
        ...         "State": "CA",
        ...         "Zip": 12345,
        ...     },
        ... }
        >>> table = MdTable(data)
        >>> print(table)
        | Name | Age | Occupation | Address.Street | Address.City | Address.State | Address.Zip |
        | --- | --- | --- | --- | --- | --- | --- |
        | John Doe | 30 | Software Engineer | 123 Main St | Anytown | CA | 12345 |
        >>> # you can also use a list of dicts
        >>> data = [
        ...     {
        ...         "Name": "John Doe",
        ...         "Age": 30,
        ...         "Occupation": "Software Engineer",
        ...     },
        ...     {
        ...         "Name": "Jane Doe",
        ...         "Age": 25,
        ...         "Occupation": "Data Scientist",
        ...     },
        ... ]
        >>> table = MdTable(data)
        >>> print(table)
        | Name | Age | Occupation |
        | --- | --- | --- |
        | John Doe | 30 | Software Engineer |
        | Jane Doe | 25 | Data Scientist |
        >>> # you can specify the precision for floats
        >>> data = {
        ...     "Name": "John Doe",
        ...     "Age": 30,
        ...     "Occupation": "Software Engineer",
        ...     "Height": 1.83,
        ...     "Weight": 80.5,
        ... }
        >>> table = MdTable(data, precision=2)
        >>> print(table)
        | Name | Age | Occupation | Height | Weight |
        | --- | --- | --- | --- | --- |
        | John Doe | 30 | Software Engineer | 1.83 | 80.50 |
    """

    def __init__(
        self,
        data: Union[Dict[str, Any], List[Dict[str, Any]]],
        transpose: bool = False,
        labels: Optional[List[str]] = None,
        precision: Union[None, int] = None,
    ):
        """Initialize a MdTable instance.

        Args:
            data (Union[Dict[str, Any], List[Dict[str, Any]]]): The data to convert.
            transpose (bool, optional): If True, transpose the table. Defaults to False.
            labels (list[str], optional): Label for header when transposed. Defaults to 'Key' and 'value {i}'.
            precision (Optional[int]): Number of decimal places for floats. If None, values are not formatted.
        """

        if isinstance(data, list):
            pass
        elif isinstance(data, dict):
            data = [data]
        else:
            raise ValueError(
                "Provided data is not a dictionary or list of dictionaries"
            )
        self.data = self._flatten_data(data)

        self.transpose = transpose
        self.precision = precision
        self.labels = labels

    def _flatten_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Flatten nested dictionaries in the data.

        Args:
            data (List[Dict[str, Any]]): The data to flatten.
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

    def dict_to_md_table(
        self,
        transpose: bool = False,
        labels: Optional[List[str]] = None,
        output_file: Union[None, str] = None,
        precision: Union[None, int] = None,
    ) -> str:
        """Convert the data to a Markdown formatted table.

        Args:
            transpose (bool, optional): If True, transpose the table. Defaults to False.
            labels (list[str], optional): Label for header when transposed. Defaults to 'Key' and 'value {i}'.
            output_file (Union[None, str], optional): The filename to write the table to.
            precision (Union[None, int], optional): The precision for floating point numbers.

        Returns:
            str: Markdown formatted table.
        """

        self.precision = precision

        md_table = ""
        if not self.data:
            return md_table

        if transpose:
            md_table = self._create_transposed_table(labels=self.labels)
        else:
            md_table = self._create_regular_table()

        if output_file:
            with open(output_file, "w") as f:
                f.write(md_table)

        return md_table

    def _create_transposed_table(self, labels: Optional[List[str]]) -> str:
        """Create a transposed version of the table.

        Args:
            key_label (str): Label for keys.
            value_label (str): Label for values.

        Returns:
            str: Markdown formatted transposed table.
        """
        transposed_data = self._transpose_data()
        if labels is None:
            labels = ["Key"] + [f"Value {i}" for i in range(len(self.data))]
        headers = self._create_transposed_headers(labels)
        table_rows = self._create_table_rows(transposed_data)

        return headers + "\n" + table_rows

    def _transpose_data(self) -> Dict[str, List[Any]]:
        """Transpose the data for creating a transposed table.

        Returns:
            dict: Transposed data as a dictionary.
        """
        headers = self.data[0].keys()
        transposed_data: Dict[str, list] = {header: [] for header in headers}
        for row in self.data:
            for key, value in row.items():
                transposed_data[key].append(value)

        return transposed_data

    def _create_transposed_headers(self, labels: List[str]) -> str:
        """Create headers for the transposed table.

        Args:
            key_label (str): Label for key.
            value_label (str): Label for values.

        Returns:
            str: Transposed table headers.
        """
        num_columns = len(self.data) + 1
        if len(labels) < len(self.data) + 1:
            warnings.warn(
                (
                    f"Number of labels ({len(labels)}) does not match "
                    f"number of columns ({num_columns}). "
                    "filling missing labels with empty strings."
                )
            )
            labels += [""] * (num_columns - len(labels))
        headers = ["---" for _ in range(num_columns)]
        return (
            f"| {labels[0]} | "
            + " | ".join([labels[i] for i in range(1, num_columns)])
            + " |\n"
            + "| "
            + " | ".join(headers)
            + " |"
        )

    def _create_regular_table(self) -> str:
        """Create a regular (non-transposed) version of the table.

        Returns:
            str: Markdown formatted table.
        """
        headers = "| " + self._create_regular_headers() + " |"
        divider = "|" + "|".join([" --- " for _ in self.data[0].keys()]) + "|"
        table_rows = self._create_regular_table_rows()

        return headers + "\n" + divider + "\n" + table_rows

    def _create_regular_headers(self) -> str:
        """Create headers for the regular table.

        Returns:
            str: Table headers.
        """
        return " | ".join(self.data[0].keys())

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

    def _create_regular_table_rows(self) -> str:
        """Create table rows for the non-transposed table.

        Returns:
            str: Formatted table rows for the regular table.
        """
        rows = []
        for row in self.data:
            rows.append(
                "| "
                + " | ".join([self._value_to_string(value) for value in row.values()])
                + " |"
            )
        return "\n".join(rows)

    def _create_table_rows(self, data: Dict[str, List[Any]]) -> str:
        """Create table rows for the given data.

        Args:
            data (Dict[str, List[Any]]): Data to be used for row creation.

        Returns:
            str: Formatted table rows.
        """
        rows = []
        for key, values in data.items():
            rows.append(
                "| "
                + key
                + " | "
                + " | ".join([self._value_to_string(value) for value in values])
                + " |"
            )
        return "\n".join(rows)

    def __str__(self) -> str:
        return self.dict_to_md_table(transpose=self.transpose, precision=self.precision)
