# mdfy Examples

This directory contains example scripts demonstrating various features of mdfy.

## Table of Contents Example

The `toc_example.py` script demonstrates how to use the Table of Contents feature in two ways:

1. **Standalone Mode**: Generate a table of contents directly from content without writing to a file
2. **With Mdfier**: Automatically generate a table of contents while writing content to a markdown file

### Running the Example

Make sure you have mdfy installed in development mode:

```bash
poetry install
```

Then run the example:

```bash
poetry run python examples/toc_example.py
```

The script will:
1. Print a standalone table of contents to the console
2. Generate a markdown file with a table of contents at `examples/output/example_with_toc.md`
3. Print the contents of the generated file