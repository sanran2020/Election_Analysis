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
# creating a file for results
csvoutfile = "election_results.csv"

# initialize total vote counter
total_votes = 0
# Candidate options
candidate_options=[]
# Declare empty dictionary
candidate_votes = {}
# initialize winning cadidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# open the election results file and read it
with open(file_to_open) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    #print(header)
    for row in csvreader:
        # Add to total vote count
        total_votes += 1
        # Print cadidate name from each row
        candidate_name = row[2]
        # Add candidate name to candidate list if its not there prior
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # initialize candidate votes
            candidate_votes[candidate_name]=0
        # add candidate votes
        candidate_votes[candidate_name] += 1

# Creating election header and writing output file
with open(csvoutfile, 'w') as txt_file:
    election_header = (
        f"--------------------------\n"
        f"Election Results\n"
        f"--------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_header, end="")
    txt_file.write(election_header)


# to do - perform analyses
for candidate_name in candidate_votes:
    # Retrieve vote count of candidate
    votes = candidate_votes[candidate_name]
    # calculate vote percentage
    vote_percentage = float(votes)/float(total_votes) * 100
    # Print candidate name and vote percentage
    candidate_results = (f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")
    print(candidate_results)
    txt_file.write(candidate_results)
    # Determine winning cadidate and votes
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name


#print(candidate_options)
#print(candidate_votes)
# Summary
Winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning vote count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n")

print(Winning_candidate_summary)
txt_file.write(Winning_candidate_summary)
# close file
#curr_dir = os.getcwd()
#print (f"Directory {curr_dir}")
csvfile.close()
txt_file.close()
