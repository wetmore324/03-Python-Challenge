import os
import csv

#Reading csv with csv module
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    #store data header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #Lists to store data
    months = []
    net_total = []
    changes = []
    previous = []
    
    #Loop through the entire list to count each month
    next(csvfile)

    total = len(months)
    for month in months:
        total += month
    print(total)      

    

