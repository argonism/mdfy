import pytest

from mdfy import MdLink


@pytest.mark.parametrize(
    "url, text, title, expected",
    [
        ("https://test.com", "", "", "[https://test.com](https://test.com)"),
        ("", "empty url", "", "[empty url]()"),
        (
            "https://another.com",
            "another link",
            "another title",
            '[another link](https://another.com "another title")',
        ),
        (None, "", None, "[]()"),
    ],
)
def test_mdlink_parametrized(url: str, text: str, title: str, expected: str) -> None:
    link = MdLink(url, text=text, title=title)
    if url is None:
        with pytest.warns(
            UserWarning, match="Link URL is None, setting to empty string"
        ):
            assert str(link) == expected
    else:
        assert str(link) == expected
