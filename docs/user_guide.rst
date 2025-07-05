===========
User Guide
===========

Welcome to the mdfy User Guide! This guide will help you get started with mdfy and explore its powerful features for creating beautiful markdown documents.

.. note::
   This guide assumes you have already installed mdfy. If you haven't, run ``pip install mdfy`` to get started.

Basic Concepts
==============

mdfy is built around the concept of **elements** and **writers**:

- **Elements**: Building blocks like headers, text, tables, and lists
- **Writers**: Tools to combine elements and output markdown

Core Elements
=============

MdHeader
--------

Create markdown headers with different levels:

.. code-block:: python

   from mdfy import MdHeader

   # Level 1 header (default)
   h1 = MdHeader("Main Title")
   print(h1)  # # Main Title

   # Level 2 header
   h2 = MdHeader("Subtitle", level=2)
   print(h2)  # ## Subtitle

   # Level 3 header
   h3 = MdHeader("Section", level=3)
   print(h3)  # ### Section

MdText
------

The most powerful element for creating formatted text:

.. code-block:: python

   from mdfy import MdText

   # Basic formatting
   text = MdText("[Hello:bold] [World:italic]!")
   print(text)  # **Hello** *World*!

   # Nested formatting
   nested = MdText("[This is [nested:bold] formatting:italic]")
   print(nested)  # *This is **nested** formatting*

   # Multiple formats
   multi = MdText("[Important:bold,italic] information")
   print(multi)  # ***Important*** information

Supported text formats:

- ``bold`` - **bold text**
- ``italic`` - *italic text*
- ``quote`` - ~~strikethrough text~~
- ``strong`` - **_strong text_**
- ``not`` - ~~strikethrough text~~

MdTable
-------

Create tables from dictionaries or lists:

.. code-block:: python

   from mdfy import MdTable

   # Simple dictionary
   data = {"Name": "John", "Age": 30, "City": "Tokyo"}
   table = MdTable(data)
   print(table)

   # List of dictionaries
   data = [
       {"Name": "Alice", "Age": 25, "City": "Tokyo"},
       {"Name": "Bob", "Age": 30, "City": "Osaka"}
   ]
   table = MdTable(data)
   print(table)

Advanced table features:

.. code-block:: python

   # Custom headers
   table = MdTable(data, header=["Full Name", "Years", "Location"])

   # Row labels
   table = MdTable(data, row_labels=["Person 1", "Person 2"])

   # Transposed table
   table = MdTable(data, transpose=True)

   # Precision for floats
   numeric_data = [{"Value": 3.14159, "Ratio": 0.6666}]
   table = MdTable(numeric_data, precision=2)

Other Elements
--------------

.. code-block:: python

   from mdfy import MdList, MdLink, MdImage, MdCode

   # Lists
   items = MdList(["Item 1", "Item 2", "Item 3"])
   numbered = MdList(["First", "Second", "Third"], ordered=True)

   # Links
   link = MdLink("https://example.com", "Example")

   # Images
   image = MdImage("path/to/image.png", "Alt text")

   # Code blocks
   code = MdCode("print('Hello, World!')", language="python")

Working with Mdfier
====================

The ``Mdfier`` class is your main tool for creating markdown documents:

.. code-block:: python

   from mdfy import Mdfier, MdHeader, MdText, MdTable

   # Create content
   content = [
       MdHeader("My Report"),
       MdText("This is a [sample:bold] report."),
       MdTable({"Metric": "Value", "Status": "OK"})
   ]

   # Write to file
   mdfier = Mdfier("report.md")
   mdfier.write(content)

Nested Content
==============

mdfy automatically flattens nested structures:

.. code-block:: python

   from mdfy import Mdfier, MdHeader, MdText

   # Nested structure
   content = [
       MdHeader("Main Section"),
       [
           MdHeader("Subsection 1", level=2),
           MdText("Content for subsection 1"),
           [
               MdHeader("Sub-subsection", level=3),
               MdText("Nested content")
           ]
       ],
       MdHeader("Another Section"),
       MdText("More content")
   ]

   Mdfier("nested.md").write(content)

Dynamic Content Generation
==========================

Combine mdfy with Python's data structures:

.. code-block:: python

   from mdfy import Mdfier, MdHeader, MdText, MdTable

   # Generate content from data
   projects = [
       {"name": "Project A", "status": "Complete", "progress": 100},
       {"name": "Project B", "status": "In Progress", "progress": 75},
       {"name": "Project C", "status": "Planned", "progress": 0}
   ]

   content = [
       MdHeader("Project Status Report"),
       MdText("Current status of all projects:"),
       MdTable(projects, precision=1)
   ]

   # Add individual project sections
   for project in projects:
       content.extend([
           MdHeader(project["name"], level=2),
           MdText(f"Status: [{project['status']:bold}]"),
           MdText(f"Progress: {project['progress']}%")
       ])

   Mdfier("project_report.md").write(content)

Best Practices
==============

1. **Use consistent heading levels**

   .. code-block:: python

      content = [
          MdHeader("Main Title"),          # Level 1
          MdHeader("Section", level=2),    # Level 2
          MdHeader("Subsection", level=3), # Level 3
      ]

2. **Leverage nested structures for organization**

   .. code-block:: python

      content = [
          MdHeader("Report"),
          [
              self.create_summary_section(),
              self.create_details_section(),
              self.create_conclusion_section()
          ]
      ]

3. **Use MdText formatting for emphasis**

   .. code-block:: python

      # Good
      MdText("This is [very important:bold] information.")

      # Avoid manual markdown
      MdText("This is **very important** information.")

4. **Customize tables for better readability**

   .. code-block:: python

      # Use meaningful headers
      table = MdTable(data, header=["Employee", "Department", "Salary"])

      # Set appropriate precision for numbers
      table = MdTable(financial_data, precision=2)

Tips and Tricks
===============

**Conditional Content**

.. code-block:: python

   content = [MdHeader("Report")]

   if include_summary:
       content.append(MdText("Summary: ..."))

   if data:
       content.append(MdTable(data))

**Reusable Components**

.. code-block:: python

   def create_status_badge(status):
       if status == "success":
           return MdText("[✅ Success:bold]")
       elif status == "warning":
           return MdText("[⚠️ Warning:bold]")
       else:
           return MdText("[❌ Error:bold]")

**Template Functions**

.. code-block:: python

   def create_report_template(title, data, summary=None):
       content = [MdHeader(title)]

       if summary:
           content.append(MdText(summary))

       content.append(MdTable(data))

       return content

Common Patterns
===============

**Data Analysis Reports**

.. code-block:: python

   def create_analysis_report(data, title="Analysis Report"):
       return [
           MdHeader(title),
           MdText(f"Analysis of {len(data)} records"),
           MdTable(data.describe().to_dict(), transpose=True),
           MdHeader("Detailed Data", level=2),
           MdTable(data.to_dict("records"))
       ]

**API Documentation**

.. code-block:: python

   def document_api_endpoint(endpoint, params, response):
       return [
           MdHeader(f"{endpoint['method']} {endpoint['path']}", level=2),
           MdText(endpoint['description']),
           MdHeader("Parameters", level=3),
           MdTable(params),
           MdHeader("Response", level=3),
           MdCode(response, language="json")
       ]

**Progress Reports**

.. code-block:: python

   def create_progress_report(tasks):
       completed = [t for t in tasks if t['status'] == 'completed']
       progress = len(completed) / len(tasks) * 100

       return [
           MdHeader("Progress Report"),
           MdText(f"Overall progress: [{progress:.1f}%:bold]"),
           MdTable(tasks, header=["Task", "Status", "Due Date"])
       ]

Troubleshooting
===============

**Common Issues**

1. **Nested brackets in MdText**

   .. code-block:: python

      # Escape brackets if they're not formatting
      MdText("Use \[brackets\] for actual brackets")

2. **Table formatting issues**

   .. code-block:: python

      # Ensure all rows have the same keys
      data = [
          {"name": "A", "value": 1},
          {"name": "B", "value": 2, "extra": "info"}  # This will cause issues
      ]

3. **File encoding problems**

   .. code-block:: python

      # Specify encoding when needed
      with open("output.md", "w", encoding="utf-8") as f:
          f.write(str(content))

Next Steps
==========

- Explore the :doc:`API Reference <mdfy>` for detailed documentation
- Check out advanced examples in the GitHub repository
- Contribute to the project by reporting issues or submitting pull requests

.. tip::
   Remember that every mdfy element can be used independently by converting it to a string with ``str(element)`` or simply printing it!