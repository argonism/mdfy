import pytest

from mdfy.elements.text import MdText


def test_plain_text():
    text = MdText("Hello World")
    assert str(text) == "Hello World"


def test_bold_text():
    text = MdText("Hello {World:bold}")
    assert str(text) == "Hello **World**"


def test_italic_text():
    text = MdText("Hello {World:italic}")
    assert str(text) == "Hello *World*"


def test_not_text():
    text = MdText("Hello {World:not}")
    assert str(text) == "Hello ~~World~~"


def test_underline_text():
    text = MdText("Hello {World:underline}")
    assert str(text) == "Hello <u>World</u>"


def test_combined_styles():
    text = MdText("{Hello:bold} {World:italic}")
    assert str(text) == "**Hello** *World*"


def test_multiple_same_styles():
    text = MdText("{Hello:bold} and {Hi:bold}")
    assert str(text) == "**Hello** and **Hi**"


def test_text_concatenation():
    text1 = MdText("{Hello:bold}")
    text2 = MdText("{World:italic}")
    combined = text1 + text2
    assert str(combined) == "**Hello***World*"


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Plain text", "Plain text"),
        ("{Hello:bold} and {World:italic}", "**Hello** and *World*"),
        ("{Hello:strong} and {World:strong}", "***Hello*** and ***World***"),
        ("{Hello:underline} and {World:underline}", "<u>Hello</u> and <u>World</u>"),
    ],
)
def test_various_texts(input_text, expected_output):
    text = MdText(input_text)
    assert str(text) == expected_output
