# === PyPoll - PYTHON CHALLENGE [MODULE 3] ===

# import modules
import os
import csv

row_count = 0

candidates = []
name_count = []
results = {}


# define filepath for source data
data_csv = os.path.join('resources','election_data.csv')

# function for calculating and displaying election results
def fn_results(row_count, candidates, name_count):

    # count results per candidate 
    r0 = (name_count.count(candidates[0]))
    r1 = (name_count.count(candidates[1]))
    r2 = (name_count.count(candidates[2]))

    # calculate percentages or results
    p0 = round((r0 / row_count * 100), 3)
    p1 = round((r1 / row_count * 100), 3)
    p2 = round((r2 / row_count * 100), 3)

    # detirmine winnter (is this where I should have used a dictionary with {candidates : [total votes, percentage of votes]) ??
    
    # something about formatting the text string below as a for loop so this code could work with any number of candidates
    
    # define results text formatting
    results_string = ('ELECTION RESULTS\n' +                                # write to file
                    '---------------------------------------\n' +
                    f'Total votes: {row_count}\n' +
                    '---------------------------------------\n' +
                    f'{candidates[0]}: {p0}% ({r0})\n' +
                    f'{candidates[1]}: {p1}% ({r1})\n' +
                    f'{candidates[2]}: {p2}% ({r2})\n' +
                    '---------------------------------------\n' +
                    f'Winner: \n' +
                    '---------------------------------------\n'
                    )

    # PRINT TO TERMINAL 
    # print(results_string)

    # WRITE RESULTS TO TXT FILE
    output_txt = os.path.join('analysis', 'final_output.old.txt')               # define filepath for outputting of results

    with open(output_txt, 'w', newline='') as txtfile:                      # open file

        txtfile.write(results_string)

# Open and read CSV file
with open(data_csv, 'r') as csvfile:

    # Split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    next(csvreader)

    # get contents
    for row in csvreader:

        # 1. Count number of rows/votes for total votes cast
        row_count += 1 

    	# 2. complete list of candidates who received votes
        candidates.append(row[2]) if row[2] not in candidates else None     # https://stackoverflow.com/questions/19834806/is-there-a-more-pythonic-way-to-prevent-adding-a-duplicate-to-a-list

        name_count.append(row[2])

# giv relevant data from CSV to function
fn_results(row_count, candidates, name_count)
# print(candidates[0])