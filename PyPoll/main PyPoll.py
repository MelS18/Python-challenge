#script for PyPoll
#import needed libraries
import os
import csv
import pathlib
from pathlib import Path

#pathlib.Path().resolve()

#dir_path = os.path.dirname(os.path.realpath(_file_))
#print("full directory: "+dir_path)

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Define Variables
votes = 0
votes_temp = 0
winner = ''
candidate_temp = ''
votes_by_candidate = []
candidates = []
# Open and read the CSV file
with open('Resources/election_data.csv', 'r') as file:
    
    csv_reader = csv.reader(file)
    
    #Exclude header
    header = next(csv_reader)
    #Loop each row to count total # of votes and find the candidates 
    for r in csv_reader:
        votes += 1
        #Review if the canditate is equal to the temp variable
        #and is not in the candidates list
        if r[2] != candidate_temp and r[2] not in candidates:
            candidates.append(r[2])
            votes_by_candidate.append(0)
            candidate_temp = r[2]
#Run a second loop to count  the votes for each candidate
#Open again the file to read from the start            
with open('Resources/election_data.csv', 'r') as file_2:
    csv_reader_2 = csv.reader(file_2)
    for j in csv_reader_2:
        for c in range(len(candidates)):
            #check who got the vote
            if j[2] == candidates[c]:
               votes_by_candidate[c] += 1 
               
#Select the winner                 
for v in range(len(votes_by_candidate)):
    if votes_by_candidate[v] > votes_temp:
        winner =  candidates[v]
        votes_temp = votes_by_candidate[v]

print("Election Results")
print("----------------------------")
print("Total Votes: {}".format(votes))

for i in range(len(candidates)):
    print("{0}: {1:.{3}f} % ({2})".format(candidates[i],  100 * votes_by_candidate[i] / votes , votes_by_candidate[i],3))
print("----------------------------")
print('Winner:', winner)

with open("Analysis/output.txt", "a") as f:
    print("Election Results", file= f)
    print("----------------------------", file= f)
    print("Total Votes: {}".format(votes), file=f)

    for i in range(len(candidates)):
        print("{0}: {1:.{3}f} % ({2})".format(candidates[i],  100 * votes_by_candidate[i] / votes , votes_by_candidate[i],3, file=f))
    print("----------------------------", file=f)
    print('Winner:', winner, file=f) 