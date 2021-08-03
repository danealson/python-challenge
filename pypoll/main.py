#Dependencies
import os
import csv

#Declare variables 
total_count = 0
votes = []
candidate_count = []
unique_candidates = []
percent = []
#vote_count = []
#vote_percent = []

#Path of CSV
election_data_csv = os.path.join("resources", "election_data.csv")

#Set to CSV
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Header
    csv_header = next(csv_reader)

    #Total Votes
    for row in csv_reader:
        total_count += 1

        #add names
        if row[2] not in unique_candidates:
                unique_candidates.append(row[2])
        
        #make a list of votes
        votes.append(row[2])

    for candidate in unique_candidates:
        candidate_count.append(votes.count(candidate))
        percent.append(round(votes.count(candidate)/total_count*100,3))

    winner = unique_candidates[candidate_count.index(max(candidate_count))]

print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_count}")
print("-----------------------------")
for i in range(len(unique_candidates)):
    print(f"{unique_candidates[i]}  {percent[i]}% ({candidate_count[i]})")
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")



output_file = 'analysis/results.txt'
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow([f"Total Votes: {total_count}"])
    csvwriter.writerow(["--------------------"])
    for i in range(len(unique_candidates)):
        csvwriter.writerow([f"{unique_candidates[i]}  {percent[i]}% ({candidate_count[i]})"])
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-----------------------------"])
    
#print(unique_candidates)
#print(total_count)


        





#Getting an error about I/O; cannot figure this out

# # You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# # The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# As an example, your analysis should look similar to the one below: