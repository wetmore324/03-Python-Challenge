import os
import csv

#Reading csv with csv module
CSV_PATH= os.path.join('Resources', 'budget_data.csv')

#set constants
MONTH_IDX = 0
PROFIT_IDX = 1

#set variables
total_profit_loss = 0
previous_profit_loss = 0
new_current_month = 0
net_change = 0
total_change = 0
greatest_gain = 0
greatest_loss = 0
greatest_gain_month = 0
greatest_loss_month = 0
month_count = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    
    for row in csvreader:
        month_count += 1
        current_month = row[MONTH_IDX]
        current_profit = int(row[PROFIT_IDX])

        #Create loop to find the profit/loss change from previous month but not including the first month
        if (month_count != 1):
            net_change = current_profit - previous_profit_loss

            if (net_change < greatest_loss):
                greatest_loss = net_change
                greatest_loss_month = current_month

            if (net_change > greatest_gain):
                greatest_gain = net_change
                greatest_gain_month = current_month

        #reset variables
        previous_profit_loss = current_profit
        previous_month = current_month

        #determine total profit/loss and also change in profit/loss for each month
        total_profit_loss = total_profit_loss + current_profit
        total_change = total_change + net_change

#print to challenge
print("Financial Analysis")
print("----------------------------------")
print("Total Months:", month_count)
print(f"Net Total Profit/Losses: ${total_profit_loss}")
print(f"Average Change: ${round(total_change / (month_count - 1), 2)}")
print(f"Greatest Increase in Profits: {greatest_gain_month} (${greatest_gain})")
print(f"Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss})")

OUT_PUT_PATH = os.path.join("analysis", "new.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(OUT_PUT_PATH, "w") as csv_out:
        csvwriter = csv.writer(csv_out, delimiter=',')
        csv_out.write("Financial Analysis\n")
        csv_out.write(f"-------------------------------\n")
        csv_out.write(f"Total Months: {month_count}\n")
        csv_out.write(f"Net Total Profit/Losses: ${total_profit_loss}\n")
        csv_out.write(f"Average Change: ${round(total_change / (month_count - 1), 2)}\n")
        csv_out.write(f"Greatest Increase in Profits: {greatest_gain_month} (${greatest_gain})\n")
        csv_out.write(f"Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss})\n")
