import os
import csv

#point to data
election_data = os.path.join('Resources', 'election_data.csv')
#output path
vote_analysis = os.path.join('output', 'vote_analysis.txt')

#define lists and variable starts
votes = []
names = []
unique_candidates = []
percentage_votes = []
total_votes = 0
votes_candidate = []


#open data and separate by dilimeter
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    #skip header row
    csv_header = next(csv_reader) #skip header row

    for row in csv_reader:
        total_votes = total_votes + 1
       

        #find the unique candidates and append them to list or add vote
        #if i need refresher - https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-pytho
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])
            index = unique_candidates.index(row[2])
            votes.append(1)
        if row[2] in unique_candidates:
            index = unique_candidates.index(row[2])            
            votes[index] += 1


    #find percentage per candidate
    percentage_results = []   
    for i in range(0, len(votes)):  
        percentage_results.append(votes[i]/total_votes)
        
    #finding winner name and index and votes
    winner_votes = max(votes)
    winner_index = votes.index(winner_votes) 
    winner_candidate = unique_candidates[winner_index]
    
 
#print results to terminal
print("Election Results")
print("------------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------------------------")
for j in range(0, len(votes)):
    print(f"{unique_candidates[j]}: {(str(round(percentage_results[j]*100,2)))}% ({str(votes[j]-1)})")
print("------------------------------------------------------")
print(f"Winner: {winner_candidate}")
print("------------------------------------------------------")


#changes amount/summary of any amount of candidates to text file in output folder
output_file = 'vote_analysis.txt'
with open('output/voter_analysis.txt', 'w') as text:
    lines = text.write("Election Result \n")
    lines = text.write("------------------------------------------------------\n")
    lines = text.write(f"Total Votes: {total_votes}\n")
    lines = text.write("------------------------------------------------------\n")
    for j in range(0, len(votes)):
        lines = text.write(f"{unique_candidates[j]}: {(str(round(percentage_results[j]*100,2)))}% ({str(votes[j]-1)})\n")
    lines = text.write("------------------------------------------------------\n")
    lines = text.write(f"Winner: {winner_candidate}\n")
    lines = text.write("------------------------------------------------------\n")
    








