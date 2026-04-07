# LD 1st
import csv
from helper_funcs import *
# Function for reading the active CSV and pulling any information for the specified time period by the user

# Find out what the current CSV is. (Columns are: day, month, year, income, expense, food(catagory), savings(catagory), any other catagories the user has made). Read the date columns and check if the parts match what the user put in.
# Example: User wants expenses from march (3) 2025 (Note, the day isn't provided so it's default will be nothing). In CSV, if month == CSV month and year == CSV year (same for day if given), add it to a list to be printed to the user. Add anything found to a list to be acessed later for printing

# Final print out example: Income and Expenses for {date}: {Full Date}: ${any income} Income, ${expense} Expenses, ${food} in Food Catagory, ${savings} in Savings catagory, *any other catagories*


# BUILD
def find_stuff_from_date(csv_path):
    def get_date_part(part):
        while True:
            num = input(f"Enter the number for {part}:\n")
            number = is_num(num)
            if number == True:
                # They entered a number. Break to move on
                return number
            else:
                print("It seems you entered something other than a number. Try again")
                continue
    
    def file_thru_csv(*num, **parts):
        # take the parts and file thru the csv. I need to know the corresponding column to check for each argument
        # If part == "year" column = 2
        # If part == "month" comunn = 1
        # If part == "day" column = 0
        found_info = []
        try:
            with open(csv_path, 'r') as file:
                content = csv.reader(file)
                headers = next(content)
                # i need to loop thru each line in csv, while looping thru each part in parts
                # This is looping thru the lines in the content, then looping thru the args and kwargs to see if the current line in loop matches
                for line in content:
                    for p, part in parts:
                        if part == "year":
                            if line[2] == num:
                                found_info.append(line)
                                continue
                            else:
                                continue
                        elif part == "month":
                            if line[1] == num:
                                found_info.append(line)
                                continue
                            else:
                                continue
                        elif part == "day":
                            if line[0] == num:
                                found_info.append(line)
                                continue
                            else:
                                continue
                        else:
                            print("Hahaha, something went very wrong. . . .")
        except Exception as e:
            print(f"Could not open file in FIND_STUFF_FROM_DATE func in get_csv_info file.\nReason: {e}")
    # user will type in day, month, and year they want to check. Tell them that if they don't want to check that catagorie, type 'none'
    # If user types 'none' for any of them, set it to 
    while True:
        type_print("1) Find by YEAR\n2) Find by MONTH\n3) Find by DAY\n4) YEAR & MONTH\n5) MONTH & DAY\n6) YEAR & DAY\n7) YEAR & MONTH & DAY\n")
        action = input("Enter the number corresponding to how you want to find information;\n")
        if action == "1":
            # year only
            year = get_date_part("year")
            file_thru_csv(year, point="year")
            break
        elif action == "2":
            # month only
            month = get_date_part('month')
            file_thru_csv(month, point="month")
            break
        elif action == "3":
            # day only
            day = get_date_part("day")
            file_thru_csv(day, point="day")
            break
        elif action == "4":
            # year and month
            year = get_date_part('year')
            month = get_date_part('month')
            file_thru_csv(year,month, point="year", point2 = "month")
            break
        elif action == "5":
            # month and day
            month = get_date_part('month')
            day = get_date_part("day")
            file_thru_csv(month,day, point="month", point2 = "day")
            break
        elif action == "6":
            # year and day
            year = get_date_part("year")
            day = get_date_part("day")
            file_thru_csv(year,day, point="year", point2 = "day")
            break
        elif action == "7":
            # All three
            year = get_date_part("year")
            month = get_date_part('month')
            day = get_date_part("day")
            file_thru_csv(year,month,day, point="year", point2 = "month",point3 = "day")
            break
        else:
            print("Invalid input. Try again")
            continue
    # have gotten all the stuff found, now disply for user
    # I dont want to parrrrrrrrrrrrrrrrrrrrrrrsssssssssssssseeeeeeeeeeeeeeeeeee thiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiisssssssssssssssssssssssssssssssssssssssssssssss
    # help