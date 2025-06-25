<p align="center">
  <br/>
  <br/>
  <picture>
    <img alt="mdfy teaser" src="https://raw.githubusercontent.com/argonism/mdfy/main/mdfy.png" style="max-width: 100%;">
  </picture>
</p>

<p align="center">
    <img alt="test" src="https://img.shields.io/github/actions/workflow/status/argonism/mdfy/test_for_pr.yml?logo=pytest&label=test&color=green">
    <img alt="latest version" src="https://img.shields.io/github/v/tag/argonism/mdfy?logo=pypi&logoColor=white&label=latest%20version">
    <img alt="issues" src="https://img.shields.io/github/issues/argonism/mdfy">
    <a href='https://mdfy.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/mdfy/badge/?version=latest' alt='Documentation Status' />
    </a>
    <img alt="PyPI dialy downloads" src="https://img.shields.io/pypi/dd/mdfy">
    <img alt="PyPI weekly downloads" src="https://img.shields.io/pypi/dw/mdfy">
    <img alt="PyPI monthly downloads" src="https://img.shields.io/pypi/dm/mdfy">
</p>

# mdfy

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

``` python
from mdfy import Mdfier, MdText, MdHeader, MdTable

contents = [
  MdHeader("Hello, MDFY!"),
  MdText("[Life:bold] is [like:italic] a bicycle."),
  MdTable({"head1": "content", "head2": "content"})
]
Mdfier("markdown.md").write(contents)

# => markdown.md
#
# # Hello, MDFY!
# **Life** is *like* a bicycle.
```

You can pass nested list to `Mdfier.write` and it will be flatterned:

``` python
from mdfy import Mdfier, MdText, MdHeader, MdTable

group = ["Group A", "Group B"]
group_agg_results = [
  [2, 3, 0, 1],
  [4, 2, 1, 0],
]

contents = [
  MdHeader("Hello, MDFY!"),
  [
    (
      MdHeader(group_name, level=2),
      MdText(f"Sum: {sum(group_agg_result)} ({', '.join(map(str, group_agg_result))})")
    )
    for group_name, group_agg_result in zip(group, group_agg_results)
  ]
]
Mdfier("markdown.md").write(contents)

# => markdown.md
# # Hello, MDFY!
# ## Group A
# Sum: 6 (2, 3, 0, 1)
# ## Group B
# Sum: 7 (4, 2, 1, 0)
```

Each mdfy element is string-convertible and can operate independently!

```python
from mdfy import MdText, MdHeader, MdTable

print(MdHeader("Hello, MDFY!"))
print(MdText("[Life:bold] is [like:italic] a bicycle."))
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
MdText("[a family:quote] of [plain-text formatting syntaxes:bold] that optionally can be [converted to [formal:italic] [markup languages:bold]:not] such as [HTML:strong]")
```

`a family` of **plain-text formatting syntaxes** that optionally can be ~~converted to _formal_ **markup languages**~~ such as **_HTML_**

See [MdText document](https://mdfy.readthedocs.io/en/latest/mdfy.elements.text.html#mdfy.elements.text.MdText) for details

## MdTable

MdTable offers a flexible way to convert a Python dict or list of dicts to a Markdown table.

```python
# Single dictionary
data = {
    "Name": "John Doe",
    "Age": 30,
    "Occupation": "Software Engineer",
}
table = MdTable(data)
print(table)

# | Name | Age | Occupation |
# | --- | --- | --- |
# | John Doe | 30 | Software Engineer |
```

You can also use custom headers:

```python
table = MdTable(data, header=["Full Name", "Years", "Job"])
print(table)

# | Full Name | Years | Job |
# | --- | --- | --- |
# | John Doe | 30 | Software Engineer |
```

For lists of dictionaries, you can add row labels:

```python
data = [
    {"Name": "John Doe", "Age": 30},
    {"Name": "Jane Doe", "Age": 25}
]
table = MdTable(data, row_labels=["Person 1", "Person 2"])
print(table)

# |  | Name | Age |
# | --- | --- | --- |
# | Person 1 | John Doe | 30 |
# | Person 2 | Jane Doe | 25 |
```

To transpose a table, pass `True` to the transpose parameter:

```python
print(MdTable(data, row_labels=["Person 1", "Person 2"], transpose=True))

# |  |  |  |
# | --- | --- | --- |
# | Name | John Doe | Jane Doe |
# | Age | 30 | 25 |
```

You can also specify custom labels when transposing and control the precision of float values:

```python
data = [
    {"precision": 0.84544, "Recall": 0.662765},
    {"precision": 0.63743, "Recall": 0.802697},
    {"precision": 0.718203, "Recall": 0.6802435},
]
labels = ["Model 1", "Model 2", "Model 3"]
print(MdTable(data, row_labels=labels, precision=3))

# | | precision | Recall |
# | --- | --- | --- |
# | Model 1 | 0.845 | 0.663 |
# | Model 2 | 0.637 | 0.803 |
# | Model 3 | 0.718 | 0.680 |
```

See [MdTable document](https://mdfy.readthedocs.io/en/latest/mdfy.elements.table.html#mdfy.elements.table.MdTable) for details

## 📖 Documentation

Check out our [full documentation](https://mdfy.readthedocs.io/en/latest/#) for detailed guides and API references.

## ✅ Testing

To run the tests:

```shell
python -m pytest
```

## 💡 Contributing

We welcome contributions!

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
