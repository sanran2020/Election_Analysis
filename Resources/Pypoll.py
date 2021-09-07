#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

import os
import csv

# Path and file to load
path_to_file = "c:/Users/15103/OneDrive/Documents/2021/Courses/Data Analytics Course/Module 3/Election_Analysis/Resources"
os.chdir(path_to_file)
file_to_open = "election_results.csv"
# open the election results file and read it
with open(file_to_open) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    print(header)
#    for row in csvreader:
        

# to do - perform analyses

# close file
curr_dir = os.getcwd()
print (f"Directory {curr_dir}")
csvfile.close()
