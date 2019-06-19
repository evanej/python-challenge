# Main Py - Homework 3
# June 15th 2019
# Evan Johnson
# PyPoll

# Step 1 - import the data
import os
import csv

poll_csv = os.path.join( 'Resources', 'election_data.csv')
pathout = os.path.join("Resources", "Election Outcomes")


total_votes = 0
winning_votes = 0
num_candidates = 0
max_votes = ["", o]
options = []
candidate_votes = []


with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        total_votes = total_votes+1 
        num_candidates = row["Candidate"]

        if row["Candidate not in options"]:
            options.append(row["Candidate"])
            candidate_votes[row["Candidate"]] = 1
       
        else
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1


# Print results