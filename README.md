# Enexis-Energy-Hub

Proof-of-concept ELT pipeline for processing smart-meter data using Python, AWS and Snowflake.

## Goal

The goal of this project is to learn about ELT / ETL pipelines and how a cloud-based data warehouse can ingest data from an external source, validate and transform it to expose usefull data for business operations.

## Architecture

-> Excel to mimic an external system 'sending' data to a webhook
-> Python to validate excel and upload the transformed CSV file to AWS as a sort of mocked smart-meter
-> AWS S3 for storage
-> AWS IAM for secure connection between AWS and Snowflake
-> Snowflake Pipe to automatically fetch new file-uploads
-> RAW layer to always keep original data
-> STAGING layer to cleanup values and validate original data's usability
-> BUSINESS layer to build meaningful views, e.g. how many unclean data was sent per day

## Packages and systems

- Python
- pandas
- boto3
- AWS S3
- AWS IAM
- Snowflake
- Snowpipe
- SQL

  ## Setup

  AWS Credentials were set up locally, IAM roles were set in AWS and are not included in this repository.

  ## Limitations

  As I have no actual way of getting data from my own smart-meter at home, the input data is now static and has to be manually edited.
  The Python script runs manually and is not scheduled.
  This is purely a proof of concept / learning project and is in no means production ready.
