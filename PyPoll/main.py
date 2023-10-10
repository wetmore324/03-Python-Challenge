import os
import csv

#Reading csv with csv module
CSV_PATH= os.path.join('Resources', 'election_data.csv')

voter_id = []
county = []
candidate = []

election_dict ={}

vote_count = 0
winner_votes = 0
winner_name = []


os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV_HEADER:{csv_header}")

    for row in csvreader:
        
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
               
        vote_count +=1
        
#print results
print("Election Results")
print("----------------------------------")
print("Total Votes:", vote_count)

#creat output path to move files to new csv text file
OUT_PUT_PATH = os.path.join("analysis", "vote.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(OUT_PUT_PATH, "w") as csv_out:
        csvwriter = csv.writer(csv_out, delimiter=',')
        csv_out.write("Election Results\n")
        csv_out.write(f"-------------------------------\n")
        csv_out.write(f"Total Votes: {vote_count}\n")
