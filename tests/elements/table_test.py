import pytest

from mdfy import MdTable


# Test initialization with dictionary
def test_initialization_with_dict():
    data = {"name": "John", "age": 30}
    table = MdTable(data)
    assert isinstance(table, MdTable)
    md_output = table.dict_to_md_table()
    expected_output = "| name | age |\n" "| --- | --- |\n" "| John | 30 |"
    assert md_output == expected_output


# Test initialization with list of dictionaries
def test_initialization_with_list():
    data = [{"name": "John", "age": 30}, {"name": "Doe", "age": 25}]
    table = MdTable(data)
    assert isinstance(table, MdTable)
    md_output = table.dict_to_md_table()
    expected_output = (
        "| name | age |\n" "| --- | --- |\n" "| John | 30 |\n" "| Doe | 25 |"
    )
    assert md_output == expected_output


# Test the creation of a regular markdown table from dictionary data
def test_dict_to_md_table():
    data = [{"name": "John", "age": 30}]
    table = MdTable(data)
    md_output = table.dict_to_md_table()
    # fmt: off
    expected_output = (
        "| name | age |\n"
        "| --- | --- |\n"
        "| John | 30 |"
    )
    # fmt: on
    assert md_output == expected_output


# Test the creation of a transposed markdown table from dictionary data
def test_transposed_table():
    data = [{"name": "John", "age": 30}]
    table = MdTable(data)
    md_output = table.dict_to_md_table(transpose=True)
    # fmt: off
    expected_output = (
        "| Key | Value 0 |\n"
        "| --- | --- |\n"
        "| name | John |\n"
        "| age | 30 |"
    )
    # fmt: on
    assert md_output == expected_output


# Test the floating point number precision
def test_precision():
    data = [{"value": 3.14159265359}]
    table = MdTable(data)
    md_output = table.dict_to_md_table(precision=2)
    # fmt: off
    expected_output = (
        "| value |\n"
        "| --- |\n"
        "| 3.14 |"
    )
    # fmt: on
    assert md_output == expected_output


# Test nested dictionary flattening
def test_flatten_dict():
    data = {"user": {"name": "John", "details": {"age": 30, "location": "Tokyo"}}}
    table = MdTable(data)
    md_output = table.dict_to_md_table()
    expected_output = (
        "| user.name | user.details.age | user.details.location |\n"
        "| --- | --- | --- |\n"
        "| John | 30 | Tokyo |"
    )
    assert md_output == expected_output


# Test MdText integration (Note: This assumes that MdText correctly processes the styled text)
def test_mdtext_integration():
    from mdfy import MdText

    data = {"text": MdText("{bold:bold}")}
    table = MdTable(data)
    md_output = table.dict_to_md_table()
    # fmt: off
    expected_output = (
        "| text |\n"
        "| --- |\n"
        "| **bold** |"
    )
    # fmt: on
    assert md_output == expected_output


# Test the exception for invalid input
def test_invalid_input():
    with pytest.raises(ValueError):
        MdTable("invalid input")
