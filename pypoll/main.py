#Dependencies
import os
import csv

#Path of CSV
election_data_csv = os.path.join("resources", "election_data.csv")

#Set to CSV
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Header
    csv_header = next(csv_reader)

#Declare variables 
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

#Total Votes
for row in csv_reader:
    count = count + 1

#Getting an error about I/O; cannot figure this out

# # You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# # The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# As an example, your analysis should look similar to the one below: