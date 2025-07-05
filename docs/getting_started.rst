===============
Getting Started
===============

Welcome to **mdfy**! This guide will help you get up and running with mdfy in just a few minutes. Whether you're new to Python or markdown generation, we'll walk you through everything step by step.

.. note::
   **What is mdfy?**

   mdfy is a Python library that makes creating beautiful markdown documents as easy as writing Python code. Instead of manually formatting markdown, you can use Python objects and let mdfy handle the formatting for you.

🚀 **Quick Installation**
=========================

Install mdfy using pip:

.. code-block:: bash

   pip install mdfy

That's it! mdfy is now ready to use.

.. tip::
   **System Requirements**

   - Python 3.9 or higher
   - No additional dependencies required for basic usage

📝 **Your First Markdown Document**
===================================

Let's create your first markdown document in just 3 lines of code:

.. code-block:: python

   from mdfy import Mdfier, MdHeader, MdText

   # Create content
   content = [
       MdHeader("My First Document"),
       MdText("Hello, **world**! This is my first mdfy document.")
   ]

   # Generate markdown file
   Mdfier("my_first_document.md").write(content)

Run this code, and you'll get a file called ``my_first_document.md`` with:

.. code-block:: markdown

   # My First Document
   Hello, **world**! This is my first mdfy document.

🎯 **Understanding the Basics**
===============================

mdfy works with two main concepts:

**Elements**
   Building blocks like headers, text, tables, and lists

**Mdfier**
   The writer that combines elements and creates markdown files

Let's explore each core element:

Headers
-------

Create headers with different levels:

.. code-block:: python

   from mdfy import MdHeader

   # Different header levels
   h1 = MdHeader("Main Title")                # # Main Title
   h2 = MdHeader("Section", level=2)          # ## Section
   h3 = MdHeader("Subsection", level=3)       # ### Subsection

Text with Formatting
--------------------

mdfy provides a special syntax for text formatting:

.. code-block:: python

   from mdfy import MdText

   # Basic formatting
   MdText("This is [bold:bold] text")                    # This is **bold** text
   MdText("This is [italic:italic] text")                # This is *italic* text
   MdText("This is [strikethrough:not] text")            # This is ~~strikethrough~~ text

   # Combined formatting
   MdText("This is [bold and italic:bold,italic] text")  # This is ***bold and italic*** text

   # Nested formatting
   MdText("This has [some [bold:bold] text:italic]")     # This has *some **bold** text*

.. note::
   **mdfy Text Formatting Syntax**

   - ``[text:bold]`` → **text**
   - ``[text:italic]`` → *text*
   - ``[text:not]`` → ~~text~~
   - ``[text:code]`` → ``text``

Tables
------

Convert Python dictionaries to markdown tables:

.. code-block:: python

   from mdfy import MdTable

   # From a dictionary
   data = {"Name": "Alice", "Age": 30, "City": "Tokyo"}
   table = MdTable(data)

   # From a list of dictionaries
   employees = [
       {"Name": "Alice", "Age": 30, "Department": "Engineering"},
       {"Name": "Bob", "Age": 25, "Department": "Sales"}
   ]
   table = MdTable(employees)

Lists
-----

Create ordered and unordered lists:

.. code-block:: python

   from mdfy import MdList

   # Unordered list
   items = MdList(["Apple", "Banana", "Cherry"])

   # Ordered list
   steps = MdList(["First step", "Second step", "Third step"], numbered=True)

🔧 **Common Patterns**
======================

Here are some patterns you'll use frequently:

Document with Multiple Sections
-------------------------------

.. code-block:: python

   from mdfy import Mdfier, MdHeader, MdText, MdTable, MdList

   # Prepare data
   team_data = [
       {"Name": "Alice", "Role": "Developer", "Experience": "5 years"},
       {"Name": "Bob", "Role": "Designer", "Experience": "3 years"}
   ]

   # Create document
   content = [
       MdHeader("Team Report"),
       MdText("This report provides an overview of our team."),

       MdHeader("Team Members", level=2),
       MdTable(team_data),

       MdHeader("Key Skills", level=2),
       MdList([
           "Python Development",
           "UI/UX Design",
           "Project Management"
       ])
   ]

   Mdfier("team_report.md").write(content)

Dynamic Content
---------------

Generate content based on data:

.. code-block:: python

   def create_summary_report(sales_data):
       total_sales = sum(item['amount'] for item in sales_data)

       return [
           MdHeader("Sales Summary"),
           MdText(f"Total sales: [${total_sales:,}:bold]"),
           MdTable(sales_data, precision=2)
       ]

   # Usage
   sales = [
       {"Product": "Laptop", "Amount": 1500.00},
       {"Product": "Phone", "Amount": 800.50}
   ]

   Mdfier("sales.md").write(create_summary_report(sales))

Nested Content
--------------

Organize content hierarchically:

.. code-block:: python

   content = [
       MdHeader("Project Documentation"),
       [
           MdHeader("Setup", level=2),
           MdText("Installation instructions..."),
           [
               MdHeader("Prerequisites", level=3),
               MdList(["Python 3.9+", "pip"])
           ]
       ],
       [
           MdHeader("Usage", level=2),
           MdText("How to use the project...")
       ]
   ]

🛠️ **Troubleshooting**
=======================

**Q: My text formatting isn't working**

Make sure you're using the correct syntax:

.. code-block:: python

   # ✅ Correct
   MdText("[Hello:bold] world")

   # ❌ Incorrect
   MdText("**Hello** world")  # This won't be processed

**Q: Table columns are misaligned**

Ensure all dictionary items have the same keys:

.. code-block:: python

   # ✅ Correct
   data = [
       {"Name": "Alice", "Age": 30},
       {"Name": "Bob", "Age": 25}
   ]

   # ❌ Problematic
   data = [
       {"Name": "Alice", "Age": 30},
       {"Name": "Bob", "Age": 25, "City": "Tokyo"}  # Extra key
   ]

**Q: Numbers in tables aren't formatted correctly**

Use the ``precision`` parameter:

.. code-block:: python

   # For financial data
   MdTable(financial_data, precision=2)  # Shows 2 decimal places

   # For integers
   MdTable(count_data, precision=0)  # No decimal places

**Q: File encoding issues**

Specify UTF-8 encoding when needed:

.. code-block:: python

   # If you encounter encoding issues
   import io

   content = [MdHeader("文档"), MdText("中文内容")]
   output = Mdfier().to_string(content)

   with open("output.md", "w", encoding="utf-8") as f:
       f.write(output)

🎯 **Next Steps**
=================

Now that you know the basics, here's what to explore next:

.. grid:: 1 2 2 2
   :gutter: 3

   .. grid-item-card:: 📖 **User Guide**
      :link: user_guide
      :link-type: doc
      :class-card: sd-text-center

      Deep dive into all mdfy features with detailed explanations and best practices.

   .. grid-item-card:: 💡 **Examples**
      :link: examples
      :link-type: doc
      :class-card: sd-text-center

      Real-world examples including reports, documentation, and data analysis.

   .. grid-item-card:: 🔧 **API Reference**
      :link: mdfy
      :link-type: doc
      :class-card: sd-text-center

      Complete API documentation for all classes and methods.

   .. grid-item-card:: 🐛 **Troubleshooting**
      :link: user_guide.html#troubleshooting
      :link-type: url
      :class-card: sd-text-center

      Solutions to common problems and advanced usage tips.

📚 **Quick Reference**
======================

.. code-block:: python

   # Essential imports
   from mdfy import Mdfier, MdHeader, MdText, MdTable, MdList

   # Basic elements
   MdHeader("Title", level=1)                    # # Title
   MdText("[Bold:bold] and [italic:italic]")     # **Bold** and *italic*
   MdTable({"key": "value"})                     # | key | value |
   MdList(["item1", "item2"])                    # - item1, - item2

   # Generate file
   Mdfier("output.md").write([...])              # Creates output.md

🎉 **You're Ready!**
====================

Congratulations! You now know enough to start creating beautiful markdown documents with mdfy.

.. tip::
   **Pro Tip**: Start small with simple documents and gradually add more complex elements as you become comfortable with the library.

Happy documenting! 🚀