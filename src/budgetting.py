import csv
import os

#Don't even understand this part

BUDGET_FILE = "budgets.csv"

if not os.path.exists(BUDGET_FILE):
    with open(BUDGET_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["category", "amount"])

#This is the end of what I don't understand        

class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = float(amount)

def add_budget():
    category = input("What is this budget for?\n")
    amount = input(f"What is the budget for {category}?\n")
    with open(BUDGET_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([category, amount])
    print(f"Budget for {category} set to ${amount}.")

def load_budgets():
    budgets = {}
    try:
        with open(BUDGET_FILE, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                budgets[row['category']] = float(row['amount'])
    except:
        pass
    return budgets

def compare_expenses_with_budget(expenses, budgets):
    report = {}
    for category, total in expenses.items():
        limit = budgets.get(category, None)
        if limit is not None:
            report[category] = (total, total <= limit)
        else:
            report[category] = (total, "No limit set")
    return report