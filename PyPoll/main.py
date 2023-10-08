import os
import csv

CVS_PATH= os.path.join('Resources', 'election_data.csv')

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header:{csv_header}")