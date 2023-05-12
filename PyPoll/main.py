import os
import csv

#Variables
total_votes = 0
candidate_list = []
candidate_votes= {}
percentage_votes_won = 0
total_votes_won = 0
popular_vote_winner = ""


#Path to Import CSV File
pypoll_file = os.path.join(".", "Resources", "election_data.csv")

#Open and Read CSV File
with open(pypoll_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

#Loop Through Rows
    last_row = ["",0]
    for row in csv_reader:
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        total_votes = total_votes + 1

#Print Total Votes
print("Election Results")

print("--------------------------")

print(f"Total Votes: {total_votes}")

print("---------------------------")

Filetowrite = os.path.join("Analysis","Election_Analysis.txc")
with open(Filetowrite, "w") as textfile:
    textfile.write(f"Election Results")

    textfile.write(f"---------------------------")

    textfile.write(f"Total Votes: {total_votes}")

    textfile.write(f"---------------------------")

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage_votes = float(votes) / float(total_votes) * 100
        if (votes > total_votes_won):
            total_votes_won = votes
            popular_vote_winner = candidate

        #Print Names/Percentage Votes/Vote Count

        print(f"{candidate}:, {percentage_votes}, {votes}")
        textfile.write(f"{candidate}:, {percentage_votes}, {votes}")   
    #Print Winner Name

    print(f"Winner: {popular_vote_winner}")
    textfile.write(f"Winner: {popular_vote_winner}")

        
