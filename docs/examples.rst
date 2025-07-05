========
Examples
========

This page showcases practical examples of using mdfy in real-world scenarios. These examples demonstrate how to leverage mdfy's features to create beautiful, structured markdown documents.

.. note::
   All examples assume you have mdfy installed. Run ``pip install mdfy`` if you haven't already.

Basic Usage Examples
====================

Simple Report
-------------

Create a basic report with headers, text, and tables:

.. code-block:: python

   from mdfy import Mdfier, MdHeader, MdText, MdTable

   # Sample data
   sales_data = [
       {"Product": "Laptop", "Units": 15, "Revenue": 22500},
       {"Product": "Phone", "Units": 28, "Revenue": 14000},
       {"Product": "Tablet", "Units": 12, "Revenue": 6000}
   ]

   # Create report
   report = [
       MdHeader("Monthly Sales Report"),
       MdText("Sales performance summary for [March 2024:bold]"),
       MdTable(sales_data, precision=0),
       MdHeader("Summary", level=2),
       MdText(f"Total products sold: [{sum(item['Units'] for item in sales_data):bold}]"),
       MdText(f"Total revenue: [${sum(item['Revenue'] for item in sales_data):,}:bold]")
   ]

   # Write to file
   Mdfier("sales_report.md").write(report)

**Output:**

.. code-block:: markdown

   # Monthly Sales Report
   Sales performance summary for **March 2024**

   | Product | Units | Revenue |
   | --- | --- | --- |
   | Laptop | 15 | 22500 |
   | Phone | 28 | 14000 |
   | Tablet | 12 | 6000 |

   ## Summary
   Total products sold: **55**
   Total revenue: **$42,500**

Project Documentation
---------------------

Generate documentation for a software project:

.. code-block:: python

   from mdfy import Mdfier, MdHeader, MdText, MdCode, MdList

   def create_project_docs(project_info):
       return [
           MdHeader(f"{project_info['name']} Documentation"),
           MdText(project_info['description']),

           MdHeader("Installation", level=2),
           MdCode(f"pip install {project_info['package_name']}", syntax="bash"),

           MdHeader("Quick Start", level=2),
           MdCode(project_info['quick_start_code'], syntax="python"),

           MdHeader("Features", level=2),
           MdList(project_info['features']),

           MdHeader("API Reference", level=2),
           MdText("For detailed API documentation, see the sections below."),
       ]

   # Project information
   project = {
       "name": "DataProcessor",
       "description": "A powerful library for [data processing:bold] and [analysis:italic].",
       "package_name": "dataprocessor",
       "quick_start_code": """from dataprocessor import DataProcessor

   dp = DataProcessor()
   result = dp.process_data(data)
   print(result)""",
       "features": [
           "Fast data processing",
           "Multiple file format support",
           "Built-in visualization tools",
           "Comprehensive error handling"
       ]
   }

   Mdfier("project_docs.md").write(create_project_docs(project))

Advanced Examples
=================

Dynamic Content Generation
---------------------------

Create reports with dynamic content based on data analysis:

.. code-block:: python

   from mdfy import Mdfier, MdHeader, MdText, MdTable
   import statistics

   def analyze_and_report(data, title="Data Analysis Report"):
       # Calculate statistics
       values = [item['value'] for item in data]
       mean_val = statistics.mean(values)
       median_val = statistics.median(values)
       std_val = statistics.stdev(values) if len(values) > 1 else 0

       # Create status based on analysis
       if mean_val > 80:
           status = "**Excellent**"
       elif mean_val > 60:
           status = "**Good**"
       else:
           status = "**Needs Improvement**"

       return [
           MdHeader(title),
           MdText(f"Analysis of {len(data)} data points"),

           MdHeader("Summary Statistics", level=2),
           MdTable([
               {"Metric": "Mean", "Value": f"{mean_val:.2f}"},
               {"Metric": "Median", "Value": f"{median_val:.2f}"},
               {"Metric": "Standard Deviation", "Value": f"{std_val:.2f}"},
               {"Metric": "Status", "Value": status}
           ]),

           MdHeader("Detailed Data", level=2),
           MdTable(data, precision=2),

           MdHeader("Recommendations", level=2),
           *generate_recommendations(mean_val, std_val)
       ]

   def generate_recommendations(mean_val, std_val):
       recommendations = []

       if mean_val < 50:
           recommendations.append(MdText("• [Action Required:bold] - Mean value is below threshold"))

       if std_val > 20:
           recommendations.append(MdText("• [High Variance:bold] - Consider investigating outliers"))

       if not recommendations:
           recommendations.append(MdText("• [No immediate action required:bold] - All metrics are within acceptable ranges"))

       return recommendations

   # Sample data
   performance_data = [
       {"Department": "Sales", "value": 85.5},
       {"Department": "Marketing", "value": 92.1},
       {"Department": "Support", "value": 78.3},
       {"Department": "Engineering", "value": 88.7}
   ]

   Mdfier("analysis_report.md").write(
       analyze_and_report(performance_data, "Q1 Performance Analysis")
   )

Multi-Section Reports
---------------------

Create complex reports with multiple sections:

.. code-block:: python

   from mdfy import Mdfier, MdHeader, MdText, MdTable, MdList

   class ReportGenerator:
       def __init__(self, title):
           self.title = title
           self.sections = []

       def add_executive_summary(self, summary_text, key_metrics):
           return [
               MdHeader("Executive Summary", level=2),
               MdText(summary_text),
               MdHeader("Key Metrics", level=3),
               MdTable(key_metrics)
           ]

       def add_data_analysis(self, data, insights):
           return [
               MdHeader("Data Analysis", level=2),
               MdTable(data, precision=2),
               MdHeader("Key Insights", level=3),
               MdList(insights)
           ]

       def add_recommendations(self, recommendations):
           return [
               MdHeader("Recommendations", level=2),
               [
                   [
                       MdHeader(f"{i+1}. {rec['title']}", level=3),
                       MdText(rec['description']),
                       MdText(f"[Priority: {rec['priority']}:bold]")
                   ]
                   for i, rec in enumerate(recommendations)
               ]
           ]

       def generate_report(self, data):
           return [
               MdHeader(self.title),
               MdText(f"Generated on: [{data['date']}:italic]"),

               self.add_executive_summary(
                   data['summary'],
                   data['key_metrics']
               ),

               self.add_data_analysis(
                   data['analysis_data'],
                   data['insights']
               ),

               self.add_recommendations(
                   data['recommendations']
               )
           ]

   # Usage
   report_gen = ReportGenerator("Q1 Business Review")

   report_data = {
       "date": "April 15, 2024",
       "summary": "Our Q1 performance shows [strong growth:bold] across all major metrics.",
       "key_metrics": [
           {"Metric": "Revenue", "Value": "$1.2M", "Change": "+15%"},
           {"Metric": "Customers", "Value": "2,450", "Change": "+12%"},
           {"Metric": "Retention", "Value": "94%", "Change": "+2%"}
       ],
       "analysis_data": [
           {"Month": "January", "Revenue": 380000, "Customers": 2100},
           {"Month": "February", "Revenue": 420000, "Customers": 2280},
           {"Month": "March", "Revenue": 450000, "Customers": 2450}
       ],
       "insights": [
           "Customer acquisition accelerated in Q1",
           "Revenue per customer increased by 8%",
           "Churn rate decreased to historic low"
       ],
       "recommendations": [
           {
               "title": "Expand Marketing Budget",
               "description": "Increase marketing spend by 20% to capitalize on current growth momentum.",
               "priority": "High"
           },
           {
               "title": "Improve Customer Onboarding",
               "description": "Streamline the onboarding process to further reduce churn.",
               "priority": "Medium"
           }
       ]
   }

   Mdfier("business_review.md").write(report_gen.generate_report(report_data))

API Documentation Generator
---------------------------

Automatically generate API documentation:

.. code-block:: python

   from mdfy import Mdfier, MdHeader, MdText, MdTable, MdCode

   def generate_api_docs(api_spec):
       docs = [
           MdHeader(f"{api_spec['name']} API Documentation"),
           MdText(api_spec['description']),
           MdText(f"Base URL: [{api_spec['base_url']}:code]"),
       ]

       for endpoint in api_spec['endpoints']:
           docs.extend([
               MdHeader(f"{endpoint['method']} {endpoint['path']}", level=2),
               MdText(endpoint['description']),

               MdHeader("Parameters", level=3),
               MdTable(endpoint['parameters']) if endpoint['parameters'] else MdText("No parameters required."),

               MdHeader("Request Example", level=3),
               MdCode(endpoint['request_example'], syntax="bash"),

               MdHeader("Response Example", level=3),
               MdCode(endpoint['response_example'], syntax="json"),

               MdHeader("Response Codes", level=3),
               MdTable(endpoint['response_codes'])
           ])

       return docs

   # API specification
   api_spec = {
       "name": "User Management",
       "description": "API for managing user accounts and profiles",
       "base_url": "https://api.example.com/v1",
       "endpoints": [
           {
               "method": "GET",
               "path": "/users",
               "description": "Retrieve a list of users",
               "parameters": [
                   {"Name": "limit", "Type": "integer", "Required": "No", "Description": "Maximum number of users to return"},
                   {"Name": "offset", "Type": "integer", "Required": "No", "Description": "Number of users to skip"}
               ],
               "request_example": "curl -X GET https://api.example.com/v1/users?limit=10&offset=0",
               "response_example": '''[
     {
       "id": 1,
       "name": "John Doe",
       "email": "john@example.com"
     }
   ]''',
               "response_codes": [
                   {"Code": "200", "Description": "Success"},
                   {"Code": "400", "Description": "Bad Request"},
                   {"Code": "401", "Description": "Unauthorized"}
               ]
           },
           {
               "method": "POST",
               "path": "/users",
               "description": "Create a new user",
               "parameters": [
                   {"Name": "name", "Type": "string", "Required": "Yes", "Description": "User's full name"},
                   {"Name": "email", "Type": "string", "Required": "Yes", "Description": "User's email address"}
               ],
               "request_example": '''curl -X POST https://api.example.com/v1/users \\
     -H "Content-Type: application/json" \\
     -d '{"name": "Jane Doe", "email": "jane@example.com"}'
   ''',
               "response_example": '''{
     "id": 2,
     "name": "Jane Doe",
     "email": "jane@example.com",
     "created_at": "2024-03-15T10:30:00Z"
   }''',
               "response_codes": [
                   {"Code": "201", "Description": "Created"},
                   {"Code": "400", "Description": "Bad Request"},
                   {"Code": "409", "Description": "Conflict - User already exists"}
               ]
           }
       ]
   }

   Mdfier("api_docs.md").write(generate_api_docs(api_spec))

Testing and QA Reports
-----------------------

Generate testing reports with detailed results:

.. code-block:: python

   from mdfy import Mdfier, MdHeader, MdText, MdTable

   def create_test_report(test_results):
       total_tests = len(test_results)
       passed = sum(1 for test in test_results if test['status'] == 'PASS')
       failed = sum(1 for test in test_results if test['status'] == 'FAIL')
       skipped = sum(1 for test in test_results if test['status'] == 'SKIP')

       pass_rate = (passed / total_tests) * 100 if total_tests > 0 else 0

       # Determine overall status
       if failed == 0:
           overall_status = "[✅ All Tests Passed:bold]"
       elif failed <= 2:
           overall_status = "[⚠️ Minor Issues:bold]"
       else:
           overall_status = "[❌ Major Issues:bold]"

       return [
           MdHeader("Test Execution Report"),
           MdText(f"Overall Status: {overall_status}"),

           MdHeader("Test Summary", level=2),
           MdTable([
               {"Metric": "Total Tests", "Value": total_tests},
               {"Metric": "Passed", "Value": passed},
               {"Metric": "Failed", "Value": failed},
               {"Metric": "Skipped", "Value": skipped},
               {"Metric": "Pass Rate", "Value": f"{pass_rate:.1f}%"}
           ]),

           MdHeader("Test Details", level=2),
           MdTable(test_results),

           MdHeader("Failed Tests", level=2) if failed > 0 else None,
           MdTable([test for test in test_results if test['status'] == 'FAIL']) if failed > 0 else MdText("No failed tests! 🎉")
       ]

   # Sample test results
   test_results = [
       {"Test Name": "test_user_login", "Status": "PASS", "Duration": "0.5s", "Module": "auth"},
       {"Test Name": "test_user_logout", "Status": "PASS", "Duration": "0.3s", "Module": "auth"},
       {"Test Name": "test_create_user", "Status": "FAIL", "Duration": "1.2s", "Module": "users"},
       {"Test Name": "test_delete_user", "Status": "PASS", "Duration": "0.8s", "Module": "users"},
       {"Test Name": "test_update_profile", "Status": "SKIP", "Duration": "0.0s", "Module": "users"}
   ]

   # Filter out None values from the report
   report_content = [item for item in create_test_report(test_results) if item is not None]

   Mdfier("test_report.md").write(report_content)

Integration Examples
====================

With Pandas DataFrames
-----------------------

Convert pandas DataFrames to markdown tables:

.. code-block:: python

   import pandas as pd
   from mdfy import Mdfier, MdHeader, MdText, MdTable

   # Create sample DataFrame
   df = pd.DataFrame({
       'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
       'Price': [999.99, 699.99, 399.99, 299.99],
       'Sales': [150, 300, 200, 75],
       'Rating': [4.5, 4.7, 4.2, 4.8]
   })

   # Convert to mdfy table
   report = [
       MdHeader("Product Analysis"),
       MdText("Current product performance metrics"),
       MdTable(df.to_dict('records'), precision=2),

       MdHeader("Summary Statistics", level=2),
       MdTable(df.describe().to_dict(), transpose=True, precision=2)
   ]

   Mdfier("product_analysis.md").write(report)

With JSON Data
--------------

Process JSON data and create structured reports:

.. code-block:: python

   import json
   from mdfy import Mdfier, MdHeader, MdText, MdTable

   # Sample JSON data
   json_data = '''
   {
       "company": "TechCorp",
       "employees": [
           {"name": "Alice Johnson", "department": "Engineering", "salary": 85000},
           {"name": "Bob Smith", "department": "Sales", "salary": 65000},
           {"name": "Carol Davis", "department": "Marketing", "salary": 70000}
       ],
       "departments": {
           "Engineering": {"budget": 500000, "head": "Alice Johnson"},
           "Sales": {"budget": 300000, "head": "Bob Smith"},
           "Marketing": {"budget": 200000, "head": "Carol Davis"}
       }
   }
   '''

   data = json.loads(json_data)

   # Create report
   report = [
       MdHeader(f"{data['company']} Employee Report"),

       MdHeader("Employee Details", level=2),
       MdTable(data['employees'], precision=0),

       MdHeader("Department Budgets", level=2),
       MdTable([
           {"Department": dept, "Budget": f"${info['budget']:,}", "Head": info['head']}
           for dept, info in data['departments'].items()
       ])
   ]

   Mdfier("employee_report.md").write(report)

Tips for Complex Documents
==========================

1. **Use helper functions** for repetitive content:

.. code-block:: python

   def create_section_header(title, level=2):
       return [
           MdHeader(title, level=level),
           MdText("---")  # Visual separator
       ]

2. **Organize content with classes** for large documents:

.. code-block:: python

   class DocumentBuilder:
       def __init__(self):
           self.sections = []

       def add_section(self, title, content):
           self.sections.append([
               MdHeader(title, level=2),
               content
           ])

       def build(self):
           return [
               MdHeader("Document Title"),
               self.sections
           ]

3. **Use conditional content** for dynamic reports:

.. code-block:: python

   content = [MdHeader("Report")]

   if include_summary:
       content.extend(create_summary_section())

   if data_available:
       content.extend(create_data_section())

4. **Create templates** for consistent formatting:

.. code-block:: python

   def create_standard_report(title, data, summary=None):
       template = [
           MdHeader(title),
           MdText(f"Generated on: {datetime.now().strftime('%Y-%m-%d')}"),
       ]

       if summary:
           template.extend([
               MdHeader("Summary", level=2),
               MdText(summary)
           ])

       template.extend([
           MdHeader("Data", level=2),
           MdTable(data)
       ])

       return template

These examples showcase the flexibility and power of mdfy for creating professional, well-structured markdown documents. Experiment with these patterns and adapt them to your specific needs!