# Python-challenge
# PyBank Instructions
Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period
# Open and read the CSV file
# Initialize variables
    total_months = 0
    net_profit_loss = 0
    profit_loss_list = []
    greatest_increase = ['', 0]
    greatest_decrease = ['', 0]
    previous_profit_loss = 0
    change_list = []
 # Loop through each row in the CSV file
 # Count the total number of months
 # Calculate the net total amount of Profit/Losses
 # Create a list of Profit/Losses values
 # Calculate the change in Profit/Losses from the previous row
 # Append the change to the list of changes in Profit/Losses
  # Check if the change is the greatest increase or decrease
  # Store the current Profit/Losses value for the next row's calculation
  # Calculate the average change in Profit/Losses
  # Print the analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

with open("Analysis/output.txt", "a") as f:
    print("Financial Analysis",file=f)
    print("----------------------------",file=f)
    print(f"Total Months: {total_months}",file=f)
    print(f"Total: ${net_profit_loss}",file=f)
    print(f"Average Change: ${avg_change:.2f}",file=f)
    print(f"Greatest Increase in Profits: {greatest_increase[0]}",file=f)
    
    
 # PyPoll Instructions
 Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote
# Define Variables
votes = 0
votes_temp = 0
winner = ''
candidate_temp = ''
votes_by_candidate = []
candidates = []
# Open and read the CSV file
 # Exclude header
 # Loop each row to count total # of votes and find the candidates
 # Review if the canditate is equal to the temp variable and is not in the candidates list
 # Run a second loop to count  the votes for each candidate
# Open again the file to read from the start   
# check who got the vote
# Select the winner
# Print the results

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

 
