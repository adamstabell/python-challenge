import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    votes = 0
    candidates = {}

    for row in csvreader:
    	votes += 1
    	candidate = row[2]
    	candidates[candidate] = candidates.get(candidate,0) + 1

newline = '\n'
analysis = f'Election Results{newline}\
Total Votes: {votes}{newline}\
{newline.join(f"{candidate}: {round((candidates[candidate] * 100 / votes),3)}% ({candidates[candidate]})" for candidate in candidates)}{newline}\
Winner: {max(candidates, key=candidates.get)}'

with open('analysis/analysis.txt', 'w') as file:
	file.write(analysis)

print(analysis)
