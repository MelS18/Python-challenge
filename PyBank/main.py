#script for PyBank
#import needed libraries
import os
import csv
import pathlib
from pathlib import Path

#pathlib.Path().resolve()

#dir_path = os.path.dirname(os.path.realpath(__file__))
#print("full directory: "+dir_path)

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Open and read the CSV file
with open('Resources/budget_data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # Skip header row
    header = next(csv_reader)

# Initialize variables
    total_months = 0
    net_profit_loss = 0
    profit_loss_list = []
    greatest_increase = ['', 0]
    greatest_decrease = ['', 0]
    previous_profit_loss = 0
    change_list = []
    # Loop through each row in the CSV file
    for row in csv_reader:

    # Count the total number of months
        total_months += 1

    # Calculate the net total amount of Profit/Losses
        net_profit_loss += int(row[1])

    # Create a list of Profit/Losses values
        profit_loss_list.append(int(row[1]))

# Calculate the change in Profit/Losses from the previous row
        if total_months > 1:
            change = int(row[1]) - previous_profit_loss
            # Append the change to the list of changes in Profit/Losses
            change_list.append(change)
            # Check if the change is the greatest increase or decrease
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = change
            elif change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change

    # Store the current Profit/Losses value for the next row's calculation
        previous_profit_loss = int(row[1])

# Calculate the average change in Profit/Losses
avg_change = sum(change_list) / len(change_list)

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