-- Create the avalanche database and schema
CREATE DATABASE IF NOT EXISTS avalanche_db;
CREATE SCHEMA IF NOT EXISTS avalanche_schema;

-- Option 1: Push files to Stage from S3
-- Create the stage for storing our files
CREATE OR REPLACE STAGE customer_reviews
  URL = 's3://sfquickstarts/misc/customer_reviews/'
  DIRECTORY = (ENABLE = TRUE AUTO_REFRESH = TRUE);

-- Option 2: Manual upload to Stage
-- Create the stage for storing our files
-- Uncomment code block below for this option
--
--CREATE STAGE IF NOT EXISTS avalanche.customer_reviews
  --ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE')
  --DIRECTORY = (ENABLE = true);
--
-- Now go and upload files to the stage. 
-- Once you've done that proceed to the next step
  
-- List the contents of the newly created stage
ls @avalanche.customer_reviews;

-- Read single file
SELECT
  SNOWFLAKE.CORTEX.PARSE_DOCUMENT(
    @avalanche.customer_reviews,
    'review-01.docx',
    {'mode': 'layout'}
  ) AS layout;
