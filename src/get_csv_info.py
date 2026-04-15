import csv
import time
from helper_funcs import *

def find_stuff_from_date(csv_path):
    def get_date_part(part):
        while True:
            num = input(f"Enter the number for {part} (or 'none' to skip):\n").strip().lower()
            if num == 'none':
                return None
            elif is_num(num):
                return num
            else:
                print("Invalid input. Try again.")

    def matches_date(line, day, month, year):
        if day is not None and line[0] != str(day):
            return False
        if month is not None and line[1] != str(month):
            return False
        if year is not None and line[2] != str(year):
            return False
        return True

    while True:
        type_print("Choose filter:\n1) Year\n2) Month\n3) Day\n4) Year & Month\n5) Month & Day\n6) Year & Day\n7) Year, Month & Day")
        action = input("Your choice:\n").strip()
        day = month = year = None
        if action == "1":
            year = get_date_part("year")
        elif action == "2":
            month = get_date_part("month")
        elif action == "3":
            day = get_date_part("day")
        elif action == "4":
            year = get_date_part("year")
            month = get_date_part("month")
        elif action == "5":
            month = get_date_part("month")
            day = get_date_part("day")
        elif action == "6":
            year = get_date_part("year")
            day = get_date_part("day")
        elif action == "7":
            year = get_date_part("year")
            month = get_date_part("month")
            day = get_date_part("day")
        else:
            print("Invalid input.")
            continue
        break

    found_info = []
    try:
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                if matches_date(line, day, month, year):
                    found_info.append(line)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    if not found_info:
        print("No data found.")
        return

    total_income = 0
    total_expense = 0
    for item in found_info:
        try:
            income = float(item[3]) if item[3] else 0
            expense = float(item[4]) if item[4] else 0
            total_income += income
            total_expense += expense
        except:
            continue

    date_str = ""
    if day:
        date_str += f"{day}/"
    if month:
        date_str += f"{month}/"
    if year:
        date_str += f"{year}"

    print(f"Summary for {date_str}:\nIncome: ${total_income:.2f}\nExpenses: ${total_expense:.2f}")
    for item in found_info:
        print(f"Day: {item[0]}, Month: {item[1]}, Year: {item[2]}, Income: {item[3]}, Expense: {item[4]}")
    time.sleep(3)