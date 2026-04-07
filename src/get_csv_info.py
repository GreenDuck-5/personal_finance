# LD 1st
# Function for reading the active CSV and pulling any information for the specified time period by the user

# Find out what the current CSV is. (Columns are: day, month, year, income, expense, food(catagory), savings(catagory), any other catagories the user has made). Read the date columns and check if the parts match what the user put in.
# Example: User wants expenses from march (3) 2025 (Note, the day isn't provided so it's default will be nothing). In CSV, if month == CSV month and year == CSV year (same for day if given), add it to a list to be printed to the user. Add anything found to a list to be acessed later for printing

# Final print out example: Income and Expenses for {date}: {Full Date}: ${any income} Income, ${expense} Expenses, ${food} in Food Catagory, ${savings} in Savings catagory, *any other catagories*

# BUILD
def find_stuff_from_date(csv_path):
    def get_date_part(part):
        print(f"Enter the number for {part}:\n")
    # user will type in day, month, and year they want to check. Tell them that if they don't want to check that catagorie, type 'none'
    # If user types 'none' for any of them, set it to 
    print("1) Find by YEAR\n2) Find by MONTH\n3) Find by DAY\n4) YEAR & MONTH\n5) MONTH & DAY\n6) YEAR & DAY\n7) YEAR & MONTH & DAY\n")
    action = input("Enter the number corresponding to how you want to find information")