-- Use correct warehouse and schema
USE WAREHOUSE ENERGY_WH;
USE DATABASE ENERGY_HUB;
USE SCHEMA PIPES;

-- Create auto-ingest pipe using earlier created Stage
CREATE PIPE ENERGY_HUB_PIPE
AUTO_INGEST = TRUE
AS COPY INTO ENERGY_HUB.INGESTION.RAW_DATA
    FROM @ENERGY_HUB.INGESTION.RAW_METER_STAGE
    FILE_FORMAT = (FORMAT_NAME = 'ENERGY_HUB.INGESTION.CSV_FORMAT');

-- Fetch SQS Queue ARN from notification_channel to post events from AWS S3
DESC PIPE ENERGY_HUB_PIPE;

-- Check pipe status
SELECT SYSTEM$PIPE_STATUS('ENERGY_HUB.PIPES.ENERGY_HUB_PIPE');

-- Check if pipe actually imported data to raw table after uploading new file
SELECT * FROM ENERGY_HUB.INGESTION.RAW_DATA;
