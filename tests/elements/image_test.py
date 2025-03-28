import logging

import pytest
from _pytest.logging import LogCaptureFixture

from mdfy import MdImage


@pytest.fixture
def basic_image() -> MdImage:
    return MdImage(src="https://example.com/image.png", alt="Example Image")


def test_basic_image_to_string(basic_image: MdImage) -> None:
    assert str(basic_image) == "![Example Image](https://example.com/image.png)"


def test_image_without_alt() -> None:
    image = MdImage(src="https://example.com/another.png")
    assert str(image) == "![](https://example.com/another.png)"


def test_image_with_special_characters() -> None:
    image = MdImage(
        src="https://example.com/image.png", alt="Image [with] (special) characters!"
    )
    expected_str = (
        "![Image [with] (special) characters!](https://example.com/image.png)"
    )
    assert str(image) == expected_str


def test_image_with_empty_src_and_alt() -> None:
    image = MdImage(src="", alt="")
    assert str(image) == "![]()"


def test_image_with_none_src(caplog: LogCaptureFixture) -> None:
    image = MdImage(src=None, alt="No Source")  # type: ignore

    assert str(image) == "![No Source]()"
    assert (
        "mdfy.elements.image",
        logging.WARNING,
        "Image source is None, setting to empty string",
    ) in caplog.record_tuples
