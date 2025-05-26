# mdfy Examples

This directory contains example scripts demonstrating various features of mdfy.

## Markdown Guide Example

The `markdown_guide.py` script demonstrates how to use various mdfy features to create a comprehensive markdown document. It shows:

- Basic text formatting
- Headers and sections
- Code blocks with syntax highlighting
- Quotes
- Links and references
- Images
- Lists (simple and nested)
- Table of contents generation
- Horizontal rules

### Running the Example

Make sure you have mdfy installed in development mode:

```bash
poetry install
```

Then run the example:

```bash
poetry run python examples/markdown_guide.py
```

The script will:
1. Generate a comprehensive markdown guide at `examples/output/markdown_guide.md`
2. Print the contents of the generated file

### Output Preview

The generated markdown file will include:
- A table of contents
- Various markdown elements with examples
- Code samples in Python and JSON
- Nested lists and formatting examples
- Best practices for using mdfy