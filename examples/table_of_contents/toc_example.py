"""
Example demonstrating the Table of Contents feature in mdfy.

This example shows two ways to use MdTableOfContents:
1. Standalone mode - generating TOC directly from content
2. With Mdfier - automatically generating TOC while writing to a file
"""

from pathlib import Path
from mdfy import (
    MdTableOfContents,
    MdHeader,
    MdText,
    MdCode,
    Mdfier,
)

# Create example content
content = [
    MdHeader("Introduction", 1),
    MdText("Welcome to the mdfy example!"),
    MdHeader("Features", 1),
    MdText("Here are some key features of mdfy:"),
    MdHeader("Table of Contents", 2),
    MdText("Automatically generate table of contents from your markdown structure."),
    MdHeader("Code Blocks", 2),
    MdCode('print("Hello, World!")', syntax="python"),
    MdHeader("Advanced Usage", 1),
    MdHeader("Configuration", 2),
    MdText("Configure mdfy to suit your needs."),
    MdHeader("Extensions", 2),
    MdText("Extend mdfy with custom elements."),
]

# Example 1: Standalone TOC generation
print("Example 1: Standalone TOC generation")
print("-" * 40)

toc = MdTableOfContents(title="Contents", level=2, contents=content)
print(str(toc))
print()

# Example 2: TOC generation with Mdfier
print("Example 2: TOC generation with Mdfier")
print("-" * 40)

# Create output directory if it doesn't exist
output_dir = Path("examples/output")
output_dir.mkdir(parents=True, exist_ok=True)

# Create markdown file with TOC
output_file = output_dir / "example_with_toc.md"
mdfier = Mdfier(output_file)

# Add TOC at the beginning and write content
mdfier.write([MdTableOfContents(title="Table of Contents", level=1), *content])

print(f"Generated markdown file at: {output_file}")
print("\nFile contents:")
print("-" * 40)
print(output_file.read_text())
