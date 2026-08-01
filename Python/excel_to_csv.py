import pandas as pandas

# read an xlsx file, to simulate data being "sent" by a meter.
excel_file = pandas.read_excel('data/Slimme Meter Data.xlsx')

# parse the data to a .csv file and save it in the data folder. This way, I can build a small Python integration to upload the csv to Amazon AWS S3.
excel_file.to_csv('data/meter_data.csv', header=True)