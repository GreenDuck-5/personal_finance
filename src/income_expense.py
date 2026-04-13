# LD Adding or removing an income/expense
import csv
import os

# Know CSV path
# Adding income/expense
# If income or expense: Know how much, add that info to current CSV (gotten from signing in)
def adding(csv_path, day, month, year, i_or_e, amount):
    # Know if income or expense so I write to the right spot
    if i_or_e == "Income":
        column = 'income'
    elif i_or_e == "Expense":
        column = 'expense'
    else:
        print("Something went wrong")
        return

    # organize the specific data to be wiritten
    data = {
        'day': day,
        'month': month,
        'year': year,
        column: amount
    }

    # write the data
    try:
        with open(csv_path, mode="a+",newline="") as file:
            reader = csv.reader(file)
            fieldname = reader.fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldname)
            writer.writerow(data)
    except Exception as e:
        print(f"Could not open file in ADDING func in income_expense file. Reason: {e}")

# Removing income/expense
# get the date and amount that was spent. Go look for that in CSV and do the in and outfile thing from previous projects of mine
def remove(csv_path, day, month, year, amount):
    # Establish the temporary name so stuff isn't confused
    temp_filename = "temp_"+csv_path

    # open an infile (current) and outfile (file that will hold same data minus the removal)
    try:
        with open(csv_path, mode='r', newline='') as infile, open(temp_filename, mode='a', newline='') as outfile:
            reader = csv.reader(infile)
            fieldname = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldname)
            writer.writeheader()

            for row in reader:
                if day ==  row[0] and month == row[1] and year == row[2] and (amount == row[3] or amount == row[4]):
                    # this means that we have encountered want we want to delete. So we dont write it and go to next iteration
                    continue
                else:
                    # the item does not match what we want gone so we write it because we want to keep it
                    writer.writerow(row)
                    
        # now that we have removed the item, replace the old file with the updated temp file and make the names the same
        os.replace(temp_filename, csv_path)
    except Exception as e:
        print(f"Could not open file in REMOVE func in income_expense file. Reason: {e}")