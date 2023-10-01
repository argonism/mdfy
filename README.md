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
  MdText("{Life:bold} is {like:italic} a bicycle.")
  MdTable(MdTable({"head1": "content", "head2": "content"}))
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
print(MdText("{Life:bold} is {like:italic} a bicycle."))
print(MdTable({"head1": "content", "head2": "content"}))

# => result
#
# # Hello, MDFY!
# **Life** is *like* a bicycle.
# | head1 | head2 |
# | --- | --- |
# | content | content |
```

## MdText Format

With MdText, you can flexibly specify text styles in a way similar to python's string formatting.

```python
MdText("{a family:underline} of {plain-text formatting syntaxes:bold} that optionally can be {converted to {formal:italic} {markup languages:bold}:underline} such as {HTML:strong}")
```

<u>a family</u> of **plain-text formatting syntaxes** that optionally can be <u>converted to _formal_ **markup languages**</u> such as **_HTML_**

## MdTable

MdTable offers a flexible way to convert a Python dict to a Markdown table.

```python
data = [
    {"precision": 0.845, "Recall": 0.662},
    {"precision": 0.637, "Recall": 0.802},
    {"precision": 0.710, "Recall": 0.680},
]

print(MdTable(data))

# The result will be
# | precision | Recall |
# | --- | --- |
# | 0.845 | 0.662 |
# | 0.637 | 0.802 |
# | 0.71 | 0.68 |
```

To transpose a table, all you need to do is pass True to the transpose parameter.

```python
print(MdTable(data, transpose=True))

# | Key | Value | Value | Value |
# | --- | --- | --- | --- |
# | name | John | Jane | Jack |
# | age | 30 | 25 | 40 |

# And you can specify header labels when transpose
labels = ["Metrics", "Model 1", "Model 2", "Model 3"]
print(MdTable(data, transpose=True, labels=labels))

# | Metrics | Model 1 | Model 2 | Model 3 |
# | --- | --- | --- | --- |
# | precision | 0.845 | 0.637 | 0.71 |
# | Recall | 0.662 | 0.802 | 0.68 |
```

You can also specify the precision of float values.

```python
data = [
    {"precision": 0.84544, "Recall": 0.662765},
    {"precision": 0.63743, "Recall": 0.802697},
    {"precision": 0.718203, "Recall": 0.6802435},
]
labels = ["Metrics", "Model 1", "Model 2", "Model 3"]
print(MdTable(data, transpose=True, labels=labels, precision=3))

# | Metrics | Model 1 | Model 2 | Model 3 |
# | --- | --- | --- | --- |
# | precision | 0.845 | 0.637 | 0.718 |
# | Recall | 0.663 | 0.803 | 0.680 |
```

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
