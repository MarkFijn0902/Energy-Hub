-- Use correct warehouse and schema
USE WAREHOUSE ENEXIS_WH;
USE DATABASE ENERGY_HUB;
USE SCHEMA PIPES;

-- Create auto-ingest pipe using earlier created Stage
CREATE OR REPLACE PIPE ENERGY_HUB_PIPE
AUTO_INGEST = TRUE
AS COPY INTO ENERGY_HUB.TABLES.RAW_METER_DATA
    FROM @ENERGY_HUB.TABLES.RAW_METER_STAGE;

-- Fetch SQS Queue ARN from notification_channel to post events from AWS S3
DESC PIPE ENERGY_HUB_PIPE;

-- Check pipe status
SELECT SYSTEM$PIPE_STATUS('ENERGY_HUB.PIPES.ENERGY_HUB_PIPE');

-- Check if pipe actually imported data to raw table
SELECT * FROM ENERGY_HUB.TABLES.RAW_METER_DATA;
