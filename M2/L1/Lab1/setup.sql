-- Create the avalanche database and schema
CREATE DATABASE IF NOT EXISTS avalanche;
CREATE SCHEMA IF NOT EXISTS avalanche;

-- Create the stage for storing our files
CREATE STAGE IF NOT EXISTS avalanche.customer_reviews
  ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE')
  DIRECTORY = (ENABLE = true);

-- Now go and upload files to the stage. 
-- Once you've done that proceed to the next step
  
-- List the contents of the newly created stage
ls @avalanche.customer_reviews;
