# M2 L2 Lab 3

In this lab, we'll build a RAG chatbot to answer questions about unstructured data (*i.e.* content from DOCX files). 

The RAG pipeline is handled by [Cortex Search](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview) where the target *chunk size* and *chunk overlap* in characters were set to 1800 and 250, respectively.
