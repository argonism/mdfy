from typing import Union

import pytest

from mdfy import MdHeader


@pytest.mark.parametrize(
    "input_text, level, expected_output",
    [
        ("Header", 1, "# Header"),
        ("Sub Header", 2, "## Sub Header"),
        ("Deeper Header", 3, "### Deeper Header"),
        ("No Level Specified", None, "# No Level Specified"),
    ],
)
def test_mdheader_formatting(
    input_text: str, level: Union[int, None], expected_output: str
) -> None:
    if level:
        header = MdHeader(input_text, level)
    else:
        header = MdHeader(input_text)
    assert str(header) == expected_output
