import pytest

from mdfy import MdHorizontal


def test_md_horizontal_default() -> None:
    md_horizontal = MdHorizontal()
    assert str(md_horizontal) == "\n***\n", "Default content should be '***'"


def test_md_horizontal_custom_content() -> None:
    custom_content = "---"
    md_horizontal = MdHorizontal(content=custom_content)
    assert (
        str(md_horizontal) == f"\n{custom_content}\n"
    ), f"Content should be '{custom_content}'"


def test_md_horizontal_non_str_content() -> None:
    with pytest.warns(UserWarning, match="Horizontal content is not a string"):
        md_horizontal = MdHorizontal(content=123)  # type: ignore
        assert (
            str(md_horizontal) == "\n123\n"
        ), "non str content should be casted to str"
