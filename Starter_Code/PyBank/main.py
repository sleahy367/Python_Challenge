import os
import csv

#Variables
total_months = 0
net_total_profit_losses = 0 
average_profit_losses = 0
max_increase_profits = {"date" : "", "amount": 0}
max_decrease_profits = {"date" : "", "amount": 0}
month_change = 0
month_change_total = 0

#Path to Import CSV File
pybank_file = os.path.join(".", "Resources", "budget_data.csv")

#Open and Read CSV File
with open(pybank_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
   
 #Loop through rows
    last_row = ["", 0]
    for row in csv_reader:
        amount = int(row[1])
        month = row[0]
        total_months = total_months + 1
        net_total_profit_losses = net_total_profit_losses + amount
        
        month_change = amount - last_row[1]
        if total_months > 1 :
            month_change_total = month_change_total + month_change
            average_profit_losses = month_change_total / (total_months - 1)
            
            if month_change > max_increase_profits["amount"]:
                max_increase_profits["amount"] = month_change
                max_increase_profits["date"] = month
            
            if month_change < max_decrease_profits["amount"]:
                max_decrease_profits["amount"] = month_change
                max_decrease_profits["date"] = month

        last_row = [month, amount]

#Print Report

print(f"Financial Analysis")

print(f"---------------------------")

print(f"Total Months: {total_months}")
print(f"Total: ${net_total_profit_losses}")
print(f"Average Change: ${average_profit_losses}")
print(f"Greatest Increase in Profits: ${max_increase_profits}")
print(f"Greatest Decrease in Profits: ${max_decrease_profits}")
