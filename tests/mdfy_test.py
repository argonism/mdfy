import tempfile

from mdfy import Mdfy, MdHeader, MdText


def test_mdfy_write():
    with tempfile.NamedTemporaryFile("w+", delete=True) as tmp:
        contents = [
            MdHeader("Hello, MDFY!"),
            MdText("[Life:bold] is [like:italic] a bicycle."),
        ]
        Mdfy(tmp.name).write(contents)

        tmp.seek(0)
        lines = tmp.readlines()

        assert lines[0] == "# Hello, MDFY!\n"
        assert lines[1] == "**Life** is *like* a bicycle.\n"


def test_mdfy_with_statement():
    with tempfile.NamedTemporaryFile("w+", delete=True) as tmp:
        contents = [MdHeader("Another Header"), MdText("[Test:bold] content.")]

        with Mdfy(tmp.name) as m:
            m.write(contents)

        tmp.seek(0)
        lines = tmp.readlines()

        assert lines[0] == "# Another Header\n"
        assert lines[1] == "**Test** content.\n"
