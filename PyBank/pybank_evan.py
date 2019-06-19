# Main Py - Homework 3
# June 15th 2019
# Evan Johnson
# Pybank

# Step 1 - import the data
import os
import csv

bank_csv = os.path.join( 'Resources', 'budget_data.csv')
pathout = os.path.join('Resources', 'Election Analysis')



with open(bank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    total = 0.0
    
    prev_row = 0

    total_changes = []

    for row in csvreader:
        rowtotal = int(row[1])
        total_changes.append(rowtotal - prev_row)
        prev_row=rowtotal
        totalmonths = 1 + len(total_changes)

#     output: (

#         "Financial Analysis\n"
#         "----------------------------\n"
#         f"Total Months: {int(totalmonths)}\n"
#         f"Average  Change: {(sum(total_changes))/(len(total_changes))}\n"
#         f"Greatest Increase Profits: {max(total_changes)}\n" 
#         f"Greatest decrease in Profits: {min(total_changes)}\n"

#         )

# print(output)
output = (
   "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {int(totalmonths)}\n"
        f"Average  Change: {(sum(total_changes))/(len(total_changes))}\n"
        f"Greatest Increase Profits: {max(total_changes)}\n" 
        f"Greatest decrease in Profits: {min(total_changes)}\n"
)

print(output)

#print the outcomes/##prints to file
output_file = os.path.join('Resources', 'financial_analysis.txt')

with open(output_file, 'w') as txtfile:
   txtfile.writelines("Financial Analysis\n")
   txtfile.writelines("--------------------\n")
   txtfile.writelines(output)
       #prints file to terminal
   with open(output_file, 'r') as readfile:

       print(readfile.read())