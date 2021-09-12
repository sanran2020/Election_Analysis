#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

import os
import csv

# Path and file to load
path_to_file = "c:/Users/15103/OneDrive/Documents/2021/Courses/Data Analytics Course/Election_Analysis/Resources"
os.chdir(path_to_file)
file_to_open = "election_results.csv"
# creating a file for results
csvoutfile = "election_results_analyses.txt"

# initialize total vote counter
total_votes = 0
# Candidate options
candidate_options=[]
#county_options
county_options=[]
# Declare empty dictionary
candidate_votes = {}
county_votes = {}
# initialize winning cadidate and winning count tracker
winning_candidate = ""
winning_count_candidate = 0
winning_percentage_candidate = 0
winning_count_county = 0
winning_percentage_county = 0
# open the election results file and read it
with open(file_to_open) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    #print(header)
    for row in csvreader:
        #print(row)
        # Add to total vote count
        total_votes += 1
        # Print cadidate name from each row
        #print(row[0])
        candidate_name = row[2]
        county_name = row[1]
        # Add candidate name to candidate list if its not there prior
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # initialize candidate votes
            candidate_votes[candidate_name]=0
        # add candidate votes
        candidate_votes[candidate_name] += 1

        if county_name not in county_options:
            county_options.append(county_name)
            # initialize county votes
            county_votes[county_name]=0
        # add candidate votes
        county_votes[county_name] += 1
# Creating election header and writing output file
with open(csvoutfile, 'w') as txt_file:
    election_header = (
        f"--------------------------\n"
        f"Election Results\n"
        f"--------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"--------------------------\n\n"
        f"--------------------------\n"
        f"County Results\n"
        f"--------------------------\n")
    print(election_header, end="")
    txt_file.write(election_header)


# to do - perform analyses
for county_name in county_votes:
    #print(candidate_votes)
    # Retrieve vote count of candidate
    votes = county_votes[county_name]
    #print(candidate_name)
    # calculate vote percentage
    vote_percentage = float(votes)/float(total_votes) * 100
    # Print candidate name and vote percentage
    county_results = (f"{county_name}: {vote_percentage: .1f}% ({votes:,})\n")
    print(county_results)
    with open(csvoutfile,'a') as txt_file:
        txt_file.write(county_results)
#Determine winning cadidate and votes
    if (votes > winning_count_county) and (vote_percentage > winning_percentage_county):
        winning_count_county = votes
        winning_percentage_county = vote_percentage
        winning_county = county_name
# County Summary
Winning_county_summary = (
    f"--------------------------\n"
    f"Largest county turnover: {winning_county}\n"
    f"--------------------------\n\n"
    f"--------------------------\n"
    f"Candidate results\n"
    f"--------------------------\n")

print(Winning_county_summary)
with open(csvoutfile,'a') as txt_file:
    txt_file.write(Winning_county_summary)



for candidate_name in candidate_votes:
    #print(candidate_votes)
    # Retrieve vote count of candidate
    votes = candidate_votes[candidate_name]
    #print(candidate_name)
    # calculate vote percentage
    vote_percentage = float(votes)/float(total_votes) * 100
    # Print candidate name and vote percentage
    candidate_results = (f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")
    print(candidate_results)
    with open(csvoutfile,'a') as txt_file:
        txt_file.write(candidate_results)
    #Determine winning cadidate and votes
    if (votes > winning_count_candidate) and (vote_percentage > winning_percentage_candidate):
        winning_count_candidate = votes
        winning_percentage_candidate = vote_percentage
        winning_candidate = candidate_name
        


#print(candidate_options)
#print(candidate_votes)
# Summary
Winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning vote count: {winning_count_candidate:,}\n"
    f"Winning Percentage: {winning_percentage_candidate:.1f}%\n"
    f"--------------------------\n")

print(Winning_candidate_summary)
with open(csvoutfile,'a') as txt_file:
    txt_file.write(Winning_candidate_summary)
# close file
#curr_dir = os.getcwd()
#print (f"Directory {curr_dir}")
#csvfile.close()
#txt_file.close()
