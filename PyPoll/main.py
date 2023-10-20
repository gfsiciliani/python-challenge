# === PyPoll - PYTHON CHALLENGE [MODULE 3] ===

# Import modules
import os
import csv

candidates = []
name_count = []
results = {}
txt_divider = '-' * 40 + '\n'

# Define filepath for source data
data_csv = os.path.join('resources','election_data.csv')

# Function for calculating and displaying election results
def fn_results(candidates, name_count):

    # Builds dictionary of unique candidates and their counts
    for x in range(len(candidates)):
        candidate_name          = candidates[x]                         # gets candidate name
        candidate_count         = name_count.count(candidates[x])       # gets candidate count
        results[candidate_name] = candidate_count                       # dictionary of unique candidate names with count as the value

    # Total results and detirmine winner
    vote_total  = sum(results.values())
    vote_top    = max(results.values())
    winner      = [name for name, votes in results.items() if votes == vote_top]

    # Defines header for printed results
    results_string = ('ELECTION RESULTS\n' +
                    f'{txt_divider}' +
                    f'Total votes: {vote_total}\n' +
                    f'{txt_divider}'
                    )

    # Calculates percentage of votes per candidate and concatenates to final output
    for x in results:
        percentage      = round((results[x] / sum(results.values()) * 100), 3)
        new_line        = f'{x}: {percentage}% ({results[x]})\n'
        results_string  = results_string + new_line

    # Concatenate and print results to terminal
    results_string = results_string + (f'{txt_divider}' +
                                       f'Winner: {winner[0]}\n' +
                                       f'{txt_divider}'
                                       )
    print(results_string)

    # Define filepath for output .txt file
    output_txt = os.path.join('analysis', 'final_output.txt')               # define filepath for outputting of results

    # Open and write to .txt file
    with open(output_txt, 'w', newline='') as txtfile:                    

        txtfile.write(results_string)

# Open and read CSV file
with open(data_csv, 'r') as csvfile:

    # Split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Store and skip header row
    header = next(csvreader)

    # get contents
    for row in csvreader:

    	# Add unique candidate names (excluding duplicates) for the purpose of complete candidate list
        candidates.append(row[2]) if row[2] not in candidates else None
        
        # Add all candidate names (including duplicates) for the purpose of vote count
        name_count.append(row[2])

# Give relevant data from CSV to function
fn_results(candidates, name_count)