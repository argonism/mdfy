.. mdfy documentation master file, created by
   sphinx-quickstart on Sat Sep 30 10:13:11 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=====================================================
mdfy - Transform text into beautiful markdown
=====================================================

.. image:: https://img.shields.io/github/actions/workflow/status/argonism/mdfy/test_for_pr.yml?logo=pytest&label=test&color=green
   :target: https://github.com/argonism/mdfy/actions
   :alt: Test Status

.. image:: https://img.shields.io/github/v/tag/argonism/mdfy?logo=pypi&logoColor=white&label=latest%20version
   :target: https://github.com/argonism/mdfy/releases
   :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/mdfy
   :target: https://pypi.org/project/mdfy/
   :alt: Downloads

Transform text into beautiful markdown, effortlessly. **mdfy** provides a simple, intuitive API for creating markdown documents programmatically with Python.

✨ **Key Features**
==================

.. grid:: 1 2 2 2
   :gutter: 3

   .. grid-item-card:: 🎯 **Simplicity**
      :class-card: sd-text-center

      Just a few lines of code and voila! An intuitive architecture made simple.

   .. grid-item-card:: 🔧 **Modularity**
      :class-card: sd-text-center

      Each module is highly independent, making it easy to use on its own.

   .. grid-item-card:: 🎨 **Customizable**
      :class-card: sd-text-center

      Extensible design allowing for easy customization.

   .. grid-item-card:: ✅ **Tested**
      :class-card: sd-text-center

      Robust unit tests ensure reliability.

🚀 **Quick Start**
==================

Installation
------------

.. code-block:: bash

   pip install mdfy

Your First Document
-------------------

.. code-block:: python

   from mdfy import Mdfier, MdHeader, MdText, MdTable

   contents = [
       MdHeader("Hello, MDFY!"),
       MdText("[Life:bold] is [like:italic] a bicycle."),
       MdTable({"head1": "content", "head2": "content"})
   ]
   Mdfier("markdown.md").write(contents)

This creates a markdown file with:

.. code-block:: markdown

   # Hello, MDFY!
   **Life** is *like* a bicycle.

   | head1 | head2 |
   | --- | --- |
   | content | content |

.. note::
   **New to mdfy?** Check out our :doc:`getting_started` guide for a step-by-step tutorial!

💡 **Advanced Usage**
====================

Nested Content
--------------

You can pass nested lists to ``Mdfier.write`` and they will be flattened:

.. code-block:: python

   from mdfy import Mdfier, MdText, MdHeader

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

Independent Elements
--------------------

Each mdfy element is string-convertible and can operate independently:

.. code-block:: python

   from mdfy import MdText, MdHeader, MdTable

   print(MdHeader("Hello, MDFY!"))
   print(MdText("[Life:bold] is [like:italic] a bicycle."))
   print(MdTable({"head1": "content", "head2": "content"}))

📖 **Documentation**
====================

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   getting_started

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   user_guide
   examples

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   mdfy
   mdfy.elements

🛠️ **Development**
==================

Want to contribute? Great! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Run tests**: ``python -m pytest``
5. **Submit a pull request**

📜 **License**
==============

This project is licensed under the MIT License. See the `LICENSE <https://github.com/argonism/mdfy/blob/main/LICENSE>`_ file for details.

🔗 **Links**
============

* 📦 `PyPI Package <https://pypi.org/project/mdfy/>`_
* 🐙 `GitHub Repository <https://github.com/argonism/mdfy>`_
* 📚 `Documentation <https://mdfy.readthedocs.io/>`_
* 🐛 `Issue Tracker <https://github.com/argonism/mdfy/issues>`_

==================
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
