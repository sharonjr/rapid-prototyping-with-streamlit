# M2 L2 Lab 3

In this lab, we'll build a RAG chatbot to answer questions about unstructured data (*i.e.* content from DOCX files). 

Briefly, the RAG pipeline that we'll use is handled by [Cortex Search](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview).

Here are 2 parameters that we'll tweak:
- *chunk size*
- *chunk overlap*
which are both set to 1800 and 250, respectively.

