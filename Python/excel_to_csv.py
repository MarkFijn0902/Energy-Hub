import pandas as pandas

# read an xlsx file, to simulate data being "sent" by a meter.
excel_file = pandas.read_excel('data/Slimme Meter Data.xlsx')

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

# parse the data to a .csv file and save it in the data folder. This way, I can build a small Python integration to upload the csv to Amazon AWS S3.
excel_file.to_csv('data/meter_data.csv', header=True)