# M2 L2 Lab 2

In this lab, we'll build a chatbot to answer questions about structured data using advanced prompting.

## Augmenting our Prompt with Data

We're converting a Pandas DataFrame into strings by appending the `.to_string()` method to the DataFrame variable. 

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

## Creating this App in Snowflake
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
