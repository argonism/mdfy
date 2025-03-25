import tempfile
from pathlib import Path

from mdfy import Mdfier, MdHeader, MdText


def test_mdfy_write() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        contents = [
            MdHeader("Hello, MDFY!"),
            MdText("[Life:bold] is [like:italic] a bicycle."),
        ]
        tmp_output_path = Path(tmp_dir, "output.md")
        Mdfier(tmp_output_path).write(contents)

        with tmp_output_path.open() as f:
            lines = f.readlines()

            assert lines[0] == "# Hello, MDFY!\n"
            assert lines[1] == "**Life** is *like* a bicycle.\n"


def test_mdfy_write_with_statement() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        contents = [
            MdHeader("Hello, MDFY!"),
            MdText("[Life:bold] is [like:italic] a bicycle."),
        ]
        tmp_output_path = Path(tmp_dir, "output.md")
        mdfier = Mdfier(tmp_output_path)
        with mdfier as mdfier:
            for content in contents:
                mdfier.write(content)

        with tmp_output_path.open() as f:
            lines = f.readlines()

            assert lines[0] == "# Hello, MDFY!\n"
            assert lines[1] == "**Life** is *like* a bicycle.\n"
            assert mdfier.file_object and mdfier.file_object.closed


def test_mdfy_write_in_utf8() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        contents = [
            MdHeader("こんにちは")
        ]
        tmp_output_path = Path(tmp_dir, "output.md")
        mdier = Mdfier(tmp_output_path)
        with mdier as mdfier:
            for content in contents:
                mdfier.write(content)

        with tmp_output_path.open(encoding="utf-8") as f:
            lines = f.readlines()

            assert lines[0] == "# こんにちは\n"
            assert mdier.file_object.closed
