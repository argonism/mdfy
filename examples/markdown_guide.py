"""
A comprehensive guide demonstrating various features of mdfy.

This example shows how to create a complete markdown document using mdfy's
different elements and features.
"""

from pathlib import Path
from typing import NoReturn

from mdfy import (
    Mdfier,
    MdTableOfContents,
    MdHeader,
    MdText,
    MdCode,
    MdQuote,
    MdLink,
    MdList,
    MdImage,
    MdHorizontal,
)


def create_markdown_guide() -> None:
    """Creates a comprehensive markdown guide using mdfy."""

    # Create the content structure
    content = [
        MdHeader("The Complete Markdown Guide", 1),
        MdText(
            "Welcome to the comprehensive guide for creating beautiful markdown documents with mdfy!"
        ),
        # Add table of contents placeholder - will be auto-generated
        MdTableOfContents(title="Contents", level=2),
        # Basic Text Formatting
        MdHeader("Basic Text Formatting", 1),
        MdText(
            "Markdown supports various text formatting options. Here's how to use them in mdfy:"
        ),
        MdList(
            [
                "Regular text is created with MdText",
                "You can use **bold** and *italic* in your text",
                "Create `inline code` by setting inline=True in MdCode",
            ]
        ),
        # Code Examples
        MdHeader("Code Examples", 1),
        MdText("mdfy makes it easy to include code snippets:"),
        MdHeader("Python Example", 2),
        MdCode(
            """def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("World"))""",
            syntax="python",
        ),
        MdHeader("JSON Example", 2),
        MdCode(
            """{
    "name": "mdfy",
    "type": "markdown",
    "awesome": true
}""",
            syntax="json",
        ),
        # Quotes
        MdHeader("Quotes", 1),
        MdText("Add memorable quotes to your documents:"),
        MdQuote("The best way to predict the future is to invent it. - Alan Kay"),
        # Links and References
        MdHeader("Links and References", 1),
        MdText("Connect your document to the web:"),
        MdList(
            [
                "[Visit mdfy Documentation](https://mdfy.readthedocs.io)",
                "[Python Official Website](https://python.org)",
                "Regular list items work too!",
            ]
        ),
        # Images
        MdHeader("Images", 1),
        MdText("Include images in your markdown:"),
        MdImage(
            src="https://www.python.org/static/community_logos/python-logo.png",
            alt="The Python Programming Language Logo",
        ),
        # Horizontal Rules
        MdHeader("Horizontal Rules", 1),
        MdText("Separate sections with horizontal rules:"),
        MdHorizontal(),
        # Lists
        MdHeader("Lists", 1),
        MdText("Create organized content with lists:"),
        MdHeader("Simple List", 2),
        MdList(["First item", "Second item", "Third item"]),
        MdHeader("Nested List", 2),
        MdList(
            [
                "Main item 1",
                MdList(["Sub item 1.1", "Sub item 1.2"], indent=2),
                "Main item 2",
                MdList(["Sub item 2.1", "Sub item 2.2"], indent=2),
            ]
        ),
        # Best Practices
        MdHeader("Best Practices", 1),
        MdText("Here are some tips for using mdfy effectively:"),
        MdList(
            [
                "Use appropriate header levels for document structure",
                "Add table of contents for longer documents",
                "Include code syntax highlighting for better readability",
                "Use descriptive alt text for images",
            ]
        ),
        # Conclusion
        MdHeader("Conclusion", 1),
        MdText(
            "Now you have a good understanding of how to use mdfy to create rich markdown documents!"
        ),
        MdQuote("Happy markdown writing with mdfy! 🎉"),
    ]

    # Create output directory
    output_dir = Path("examples/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Write the markdown guide
    output_file = output_dir / "markdown_guide.md"
    mdfier = Mdfier(output_file)
    mdfier.write(content)

    print(f"Generated markdown guide at: {output_file}")
    print("\nFile contents:")
    print("-" * 40)
    print(output_file.read_text())


if __name__ == "__main__":
    create_markdown_guide()
