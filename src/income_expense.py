import csv
import os

def adding(csv_path, day, month, year, i_or_e, amount):
    if i_or_e == "Income":
        column = 'income'
    elif i_or_e == "Expense":
        column = 'expense'
    else:
        print("Invalid type.")
        return

    data = {
        'day': day,
        'month': month,
        'year': year,
        'income': '',
        'expense': ''
    }
    data[column] = amount

    try:
        with open(csv_path, mode="a+", newline='') as file:
            file.seek(0)
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)
    except Exception as e:
        print(f"Could not open file in ADDING. Reason: {e}")

def remove(csv_path, day, month, year, amount):
    temp_filename = "temp_" + csv_path
    try:
        with open(csv_path, mode='r', newline='') as infile, open(temp_filename, mode='w', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                if row['day'] == str(day) and row['month'] == str(month) and row['year'] == str(year):
                    if row['income'] == str(amount) or row['expense'] == str(amount):
                        continue
                writer.writerow(row)
        os.replace(temp_filename, csv_path)
    except Exception as e:
        print(f"Could not open file in REMOVE. Reason: {e}")