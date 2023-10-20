# === PyBank - PYTHON CHALLENGE [MODULE 3] ===

# Import modules
import os
import csv

# Define initial variables
total_profit    = 0
row_count       = 0
monthly_change  = {}

# Define filepath for source data
data_csv = os.path.join('resources','budget_data.csv')

# Function accepting relevant data from csvreader
def fn_bank(row_count, total_profit, monthly_change):

    # Calculate and store values for changes [max, min, avg]
    max_change = max(monthly_change.values())
    min_change = min(monthly_change.values())
    avg_change = sum(monthly_change.values()) / len(monthly_change)
    
    # Get months for max/min changes
    max_change_month = max(monthly_change, key=monthly_change.get)
    min_change_month = min(monthly_change, key=monthly_change.get)

    # Trim avg_change to two decimal places with proper rounding
    avg_change_formatted = round(avg_change, 2) 

    # Write results to .txt file
    output_txt = os.path.join('analysis', 'final_output.txt')               # define filepath for outputting of results

    with open(output_txt, 'w', newline='') as txtfile:                      # open file

        txtfile.write('FINANCIAL ANALYSIS\n' +                              # write to file
                    '---------------------------------------\n' +
                    f'Total months: {row_count}\n' +
                    f'Total: ${total_profit}\n' +
                    f'Average change: ${avg_change_formatted}\n' +
                    f'Greatest increase in profits: {max_change_month} (${max_change})\n' +
                    f'Greatest decrease in profits: {min_change_month} (${min_change})\n'
                    )

# Open and read CSV file
with open(data_csv, 'r') as csvfile:

    # Split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    header = next(csvreader)

    # Get contents
    for row in csvreader:
        
        # Store value of present row
        current_val = int(row[1]) 

        # Increment row counter (to be used for counting total_months and calculating change values)
        row_count += 1

        # Total profit losses
        total_profit = total_profit + int(row[1])
        
        # Calculate CHANGE between month profits
        if row_count > 1:                               # conditional to disregard first row of data being counted as a change                                        
            change_val = current_val - previous_val     # calculate change
            monthly_change[row[0]] = change_val         # store changes in dictionary

        # Store previous_val for next loop
        previous_val = current_val

# Give relevant data to function for final calculations and output
fn_bank(row_count, total_profit, monthly_change)