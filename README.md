![mdfy logo](teaser.png)

# mdfy

<!-- ![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/argonism/mdfy)
![Issues](https://img.shields.io/github/issues/your_username/mdfy) -->

Transform text into beautiful markdown, effortlessly.

<!-- <p align="center">
  <img src="path_to_your_project_logo_or_image" alt="MDFY Logo" width="400">
</p> -->

## 🌟 Features

- **Simplicity**: Just a few lines of code and voila! An intuitive architecture made simple.
- **Modulability**: Each module is highly independent, making it easy to use on its own.
- **Customizable**: Extensible design allowing for easy customization.
- **Highly Tested**: Robust unit tests ensure reliability.

## 🚀 Getting Started

### Installation

```shell
pip install mdfy
```

### Usage

Here's a quick start guide to get you up and running!

```python
from mdfy import Mdfier, MdText, MdHeader

contents = [
  MdHeader("Hello, MDFY!"),
  MdText("[Life:bold] is [like:italic] a bicycle.")
]
Mdfy("markdown.md").write(contents)

# => markdown.md
#
# # Hello, MDFY!
# **Life** is *like* a bicycle.
```

Each mdfy element is string-convertible and can operate independently!

```python
from mdfy import MdText, MdHeader, MdTable

print(MdHeader("Hello, MDFY!"))
print(MdText("[Life:bold] is [like:italic] a bicycle."))
print(MdTable({"head1": "content", "head2": "content"}, transpose=True))

# => result
#
# # Hello, MDFY!
# **Life** is *like* a bicycle.
# | Key | Value |
# | --- | --- |
# | head1 | content |
# | head2 | content |
```

### MdText の記法

## 📖 Documentation

Check out our [full documentation](link_to_your_documentation) for detailed guides and API references.

## ✅ Testing

To run the tests:

```shell
python -m pytest
```

## 💡 Contributing

We welcome contributions!

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
