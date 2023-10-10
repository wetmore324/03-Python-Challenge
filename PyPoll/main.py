import os
import csv

#Reading csv with csv module
CSV_PATH= os.path.join('Resources', 'election_data.csv')

vote_count = 0
counter = 0


os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header:{csv_header}")

    for row in csvreader:
        vote_count += 1
        from collections import Counter

        def count_candidates (csvfile):
            candidate_counter = Counter()
            with open(csvfile) as file:
                for line in file:
                    line_candidate

    print(vote_count)