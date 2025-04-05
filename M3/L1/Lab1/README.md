# M3 L1 Lab 1

In this lab, we're aggregating all that we've built in prior labs into this Streamlit app that we'll deploy to Streamlit in Snowflake (SiS).

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
