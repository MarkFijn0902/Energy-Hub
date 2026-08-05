import pandas
import boto3
from datetime import datetime

def main():
    # read an xlsx file, to simulate data being "sent" by a meter.
    excel_file = pandas.read_excel('data/Slimme Meter Data.xlsx')

    validate_excel(excel_file)    

    # parse the data to a .csv file and save it in the data folder. This way, I can build a small Python integration to upload the csv to Amazon AWS S3.
    csv_file = excel_file.to_csv('data/generated_meter_data.csv', index=False, header=True)

    upload_csv_to_s3()

def validate_excel(excel_file):
    # Expected values to ensure incoming data has the correct columns
    expected_columns = [
        'reading_id',
        'meter_id',
        'timestamp',
        'location',
        'energy_consumption_kwh',
        'solar_generation_kwh',
        'voltage',
        'current_temperature_c'
    ]

    # Raise exception for missing columns
    for column in expected_columns:
        if column not in excel_file.columns:
            raise Exception(f"Not all columns were present, missing column: {column}")

    # Raise exception when excel is empty
    if excel_file.empty:
        raise Exception("No data found in excel file")

def upload_csv_to_s3():
    # create s3 client and upload file to Amazon S3
    s3_client = boto3.client('s3')
    file_name = f"raw/meter_data_{datetime.now():%Y%m%d_%H%M%S}.csv"

    s3_client.upload_file('data/generated_meter_data.csv', 'amazon-s3-enexis-raw-data', file_name)

if __name__ == "__main__":
    main()
