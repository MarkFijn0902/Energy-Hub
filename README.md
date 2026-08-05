# Energy-Hub - Smart-Meter proof of concept

Proof-of-concept ELT pipeline for processing smart-meter data using Python, AWS and Snowflake.

## Goal

The goal of this project is to learn about ELT / ETL pipelines and how a cloud-based data warehouse can ingest data from an external source, validate and transform it to expose useful data for business operations.
For this project, I chose to work with views in my staging and business layer, as they will automatically change when new data is added by SnowPipe. Learning and investigating how Matillion works seemed overkill for my demonstration purposes.
Input data was generated using ChatGPT for demonstration purposes.

## Architecture

```
-> Excel to mimic an external system 'sending' data to a webhook
-> Python to validate excel and upload the transformed CSV file to AWS as a sort of mocked smart-meter
-> AWS S3 for storage
-> AWS IAM for secure connection between AWS and Snowflake
-> Snowflake Pipe to automatically fetch new file-uploads
-> RAW layer to always keep original data
-> STAGING layer to cleanup values and validate original data's usability
-> BUSINESS layer to build meaningful views, e.g. how much invalid invalid data was sent
```

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

## Screenshots

- Database tree view:
<img width="281" height="538" alt="image" src="https://github.com/user-attachments/assets/1f10ff5d-a9c0-4a3c-b93d-fd9f1b93faa5" />

- Raw data inside the Ingestion.RAW_DATA table:
<img width="2141" height="1185" alt="image" src="https://github.com/user-attachments/assets/c33d963c-dcfc-4507-b405-4b45567f0a08" />

- Cleaned data inside STAGING view:
<img width="2108" height="1201" alt="image" src="https://github.com/user-attachments/assets/d7ad1bc9-f279-4192-9243-1e87ee1885e4" />

- Running Pipe:
<img width="2160" height="215" alt="image" src="https://github.com/user-attachments/assets/0f96145d-0fc3-4b69-8d3e-580b3a27813b" />

- Quality Status BUSINESS view:
<img width="2149" height="541" alt="image" src="https://github.com/user-attachments/assets/bf79d82b-1be4-4f9e-bf15-48eae906345e" />


