# M1 Lab 3

In this third lab, we'll build the dashboard of the Avalanche customer review data app. 

## Setup of database and schema

In this folder, you'll also see a `setup.sql` file that provides the necessary SQL query that you can use to create the `avalanche_db` database and `avalanche_schema` that we'll use in this app as well as used in further labs in this course. 
```sql
CREATE DATABASE IF NOT EXISTS avalanche_db;
CREATE SCHEMA IF NOT EXISTS avalanche_schema;
```

## Creating this Streamlit App in Snowflake
- **Step 1.** Download the file called streamlit_app.py from this folder in the course Github Repo.
- **Step 2.** After enrolling in your free Snowflake trial account at https://signup.snowflake.com/?trial=student&cloud=aws&region=us-west-2, then log in to Snowflake Snowsight

Approach 1:

- **Step 3A.** In the left sidebar, click on "Projects" > "Streamlit" to bring up the Streamlit workspace
- **Step 3B.** In the top-right corner, click on "+ Streamlit App" to create a Streamlit app.

Approach 2:

- **Step 3.** In the left sidebar, click on + "Create" > "Streamlit App"
- **Step 4.** A "Create Streamlit App" modal window pops up. Enter the following:

Final Step: 
- **Step 5.** Follow along with the lab video called “Lab Overview- Building a Simple GenAI App”.

