# import necessary packages
import os
import csv

# Specify the CSV path
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    month_counter = 0
    profit_loss = 0
    delta_pl = 0
    Max_increase = 0
    Max_decrease = 0

    for row in csvreader:
    	# Determine the total number of months included in the dataset
    	month_counter += 1

    	# Determine the net total amount of "Profit/Losses" over the entire period
    	profit_loss = profit_loss + int(row[1])

    	# Calculate the changes in "Profit/Losses" over the entire period,
    	if month_counter > 1:
    		delta_pl += int(row[1]) - last_pl

    		# Determine the greatest increase in profits (date and amount) over the entire period
    		if (int(row[1]) - last_pl) > Max_increase:
    			Max_increase = int(row[1]) - last_pl
    			Max_month_up = row[0]

    		# Determine the greatest decrease in losses (date and amount) over the entire period
    		elif (int(row[1]) - last_pl) < Max_decrease:
    			Max_decrease = int(row[1]) - last_pl
    			Max_month_down = row[0]

    	last_pl = int(row[1])


# then find the average of those changes
avg_delta_pl = delta_pl / (month_counter - 1)

# Save file and print the results to the terminal
newline = '\n'
analysis = f'Total Months: {month_counter}{newline}\
Total: ${profit_loss}{newline}\
Average Change: ${round(avg_delta_pl, 2)}{newline}\
Greatest Increase in Profits: {Max_month_up} (${Max_increase}){newline}\
Greatest Decrease in Profits: {Max_month_down} (${Max_decrease})'

with open('analysis/analysis.txt', 'w') as file:
	file.write(analysis)

print(analysis)