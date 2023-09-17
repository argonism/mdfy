import pytest

from mdfy.elements.header import MdHeader


@pytest.mark.parametrize(
    "input_text, level, expected_output",
    [
        ("Header", 1, "# Header"),
        ("Sub Header", 2, "## Sub Header"),
        ("Deeper Header", 3, "### Deeper Header"),
        ("No Level Specified", None, "# No Level Specified"),
    ],
)
def test_mdheader_formatting(input_text, level, expected_output):
    if level:
        header = MdHeader(input_text, level)
    else:
        header = MdHeader(input_text)
    assert str(header) == expected_output
