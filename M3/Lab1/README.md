# M3 Lab 1

In this lab, we'll build a chatbot to answer questions about structured data using advanced prompting.

You can think of this as a RAG chatbot over structured data; with the caveat that we're not using vector embeddings and vector databases; instead we're applying the string version of the DataFrame as context directly in the prompt.

## Setup

In M2 Lab 1, we've exported the processed Avalanche structured data, which we'll need in this lab. As we had already uploaded this processed CSV data (using a previously prepared data) into Snowflake in M1 Lab 3 at `AVALANCHE_DB.PUBLIC.CUSTOMER_REVIEWS` we can now readily use it.

## Augmenting our Prompt with Data

After reading in the CSV data into a Pandas DataFrame, we're converting it into strings by appending the `.to_string()` method to the DataFrame variable. 

The resulting string is represented by `{dataframe_context}` that is then added to `<context></context>`.

Here's the prompt:
```
[INST]
You are a helpful AI chat assistant. Answer the user's question based on the provided
chat history and the context data from customer reviews provided below.

Use the data in the <context> section to inform your answer about customer reviews or sentiments
if the question relates to it. If the question is general and not answerable from the context
or chat history, answer naturally. Do not explicitly mention "based on the context" unless necessary for clarity.

<chat_history>
{chat_history}
</chat_history>

<context>
{dataframe_context}
</context>

<question>
{user_question}
</question>
[/INST]
Answer:
```

## Creating this Streamlit App in Snowflake
- **Step 1.** Log in to Snowflake Snowsight

Approach 1:

- **Step 2A.** In the left sidebar, click on "Projects" > "Streamlit" to bring up the Streamlit workspace
- **Step 2B.** In the top-right corner, click on "+ Streamlit App" to create a Streamlit app.

Approach 2:

- **Step 2.** In the left sidebar, click on + "Create" > "Streamlit App"

- **Step 3.** A "Create Streamlit App" modal window pops up. Enter the following:

  - App title
  - App location: choose database and choose schema
  - App warehouse

- **Step 4.** An example Streamlit app should appear
- **Step 5.** Paste the code content from the `streamlit_app.py` in this sub-directory into the left code editor panel.
