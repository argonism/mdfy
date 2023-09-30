from mdfy import MdCode


def test_mdcode_inline():
    code = MdCode("ls -la", inline=True)
    assert str(code) == "`ls -la`"


def test_mdcode_block_with_newline():
    code_content = "print('Hello, World!')\nprint('MDFY!')"
    code = MdCode(code_content)
    expected = "```\nprint('Hello, World!')\nprint('MDFY!')\n```"
    assert str(code) == expected


def test_mdcode_block_without_newline():
    code_content = "print('Hello, World!')"
    code = MdCode(code_content)
    expected = "```\nprint('Hello, World!')\n```"
    assert str(code) == expected


def test_mdcode_with_syntax():
    code_content = "print('Hello, World!')"
    code = MdCode(code_content, syntax="python")
    expected = "```python\nprint('Hello, World!')\n```"
    assert str(code) == expected


def test_mdcode_inline_override_with_newline():
    # even if inline=True, presence of newline in code should override to block
    code_content = "print('Hello, World!')\nprint('MDFY!')"
    code = MdCode(code_content, inline=True)
    expected = "```\nprint('Hello, World!')\nprint('MDFY!')\n```"
    assert str(code) == expected


def test_mdcode_none_content():
    code = MdCode(None)
    assert str(code) == "```\n\n```"
