USE DATABASE ENERGY_HUB;
USE SCHEMA INGESTION;

-- Create the integration
CREATE STORAGE INTEGRATION RAW_METER_INTEGRATION
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = 's3'
STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::685394895735:role/EnergyHubRole'
STORAGE_ALLOWED_LOCATIONS = ( 's3://amazon-s3-enexis-raw-data/raw/' )
ENABLED = TRUE;

-- Fetch ARN and external id for AWS IAM Role
DESC STORAGE INTEGRATION RAW_METER_INTEGRATION;

-- Create a csv file format to skip the header
CREATE FILE FORMAT CSV_FORMAT
TYPE = CSV
SKIP_HEADER = 1;

-- Create an external stage to pull data from S3
CREATE STAGE RAW_METER_STAGE
URL = 's3://amazon-s3-enexis-raw-data/raw/'
STORAGE_INTEGRATION = RAW_METER_INTEGRATION
FILE_FORMAT = 'CSV_FORMAT';

-- Be sure to use the correct schema
USE DATABASE ENERGY_HUB;
USE SCHEMA TABLES;

-- Copy into command to test the external stage
COPY INTO ENERGY_HUB.INGESTION.RAW_METER_TABLE
    FROM @RAW_METER_STAGE;
