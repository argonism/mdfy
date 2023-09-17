from typing import Any, Dict, List, Union

from ._base import MdElement


class MdTable(MdElement):
    def __init__(self, data, transpose=False, precision=None):
        """
        Initialize the converter with given data.

        Args:
            data (dict or list): The data to convert.
            transpose (bool, optional): If True, transpose the table. Defaults to False.
            precision (Optional[int]): Number of decimal places for floats. If None, values are not formatted.
        """
        if isinstance(data, dict):
            self.data = [data]
        elif isinstance(data, list):
            self.data = data
        else:
            raise ValueError(
                "Provided data is not a dictionary or list of dictionaries"
            )
        self.transpose = transpose
        self.precision = precision
        self._flatten_data()

    def _flatten_data(self):
        """
        Flatten nested dictionaries in the data.
        """
        flattened_data = []
        for entry in self.data:
            flattened_data.append(self._flatten_dict(entry))

        self.data = flattened_data

    def _flatten_dict(self, d: Dict, parent_key: str = "", sep: str = ".") -> Dict:
        """
        Recursively flatten a nested dictionary.

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
        key_label: str = "Key",
        value_label: str = "Value",
        output_file: Union[None, str] = None,
        precision: Union[None, int] = None,
    ) -> str:
        """
        Convert the data to a Markdown formatted table.

        Args:
            transpose (bool, optional): If True, transpose the table. Defaults to False.
            key_label (str, optional): Label for keys when transposed. Defaults to 'Key'.
            value_label (str, optional): Label for values when transposed. Defaults to 'Value'.
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
            md_table = self._create_transposed_table(key_label, value_label)
        else:
            md_table = self._create_regular_table()

        if output_file:
            with open(output_file, "w") as f:
                f.write(md_table)

        return md_table

    def _create_transposed_table(self, key_label, value_label):
        """
        Create a transposed version of the table.

        Args:
            key_label (str): Label for keys.
            value_label (str): Label for values.

        Returns:
            str: Markdown formatted transposed table.
        """
        transposed_data = self._transpose_data()
        headers = self._create_transposed_headers(key_label, value_label)
        table_rows = self._create_table_rows(transposed_data)

        return headers + "\n" + table_rows

    def _transpose_data(self):
        """
        Transpose the data for creating a transposed table.

        Returns:
            dict: Transposed data as a dictionary.
        """
        headers = self.data[0].keys()
        transposed_data = {header: [] for header in headers}
        for row in self.data:
            for key, value in row.items():
                transposed_data[key].append(value)

        return transposed_data

    def _create_transposed_headers(self, key_label: str, value_label: str) -> str:
        """
        Create headers for the transposed table.

        Args:
            key_label (str): Label for key.
            value_label (str): Label for values.

        Returns:
            str: Transposed table headers.
        """
        headers = ["---" for _ in range(len(self.data) + 1)]
        return (
            f"| {key_label} | "
            + " | ".join([value_label for i in range(len(self.data))])
            + " |\n"
            + "| "
            + " | ".join(headers)
            + " |"
        )

    def _create_regular_table(self) -> str:
        """
        Create a regular (non-transposed) version of the table.

        Returns:
            str: Markdown formatted table.
        """
        headers = "| " + self._create_regular_headers() + " |"
        divider = "|" + "|".join([" --- " for _ in self.data[0].keys()]) + "|"
        table_rows = self._create_regular_table_rows()

        return headers + "\n" + divider + "\n" + table_rows

    def _create_regular_headers(self) -> str:
        """
        Create headers for the regular table.

        Returns:
            str: Table headers.
        """
        return " | ".join(self.data[0].keys())

    def _value_to_string(self, value: Any) -> str:
        """
        Convert the given value to a string. If it's a floating point number,
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
        """
        Create table rows for the non-transposed table.

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

    def _create_table_rows(
        self, data: Union[Dict[str, Any], List[Dict[str, Any]]]
    ) -> str:
        """
        Create table rows for the given data.

        Args:
            data (Union[Dict[str, Any], List[Dict[str, Any]]]): Data to be used for row creation.

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

    def __str__(self):
        return self.dict_to_md_table(transpose=self.transpose, precision=self.precision)
