# M2 L1 Lab 1

In this lab, we'll prepare the Avalanche data namely the Customer Reviews subset from an unstructured format to a structured format in a Snowflake Notebooks.

## Data Processing

Here, we're leveraging Snowflake Cortex to perform the following data processing tasks:
- `PARSE_DOCUMENT` function to extract text and data from unstructured DOCX files.
- `SENTIMENT` function to calculate the sentiment score of extracted customer review text
- `SUMMARIZE` function to return a concise summary of the customer review text
- `TRANSLATE:` function to translate given text from/to any supported language

## Data Visualization

Next, we'll use the structured data to create a bar chart to visualize the daily sentiment score and the product sentiment score.
