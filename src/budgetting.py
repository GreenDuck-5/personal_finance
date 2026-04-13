#DJ, 1st, Budgetting Program


# add budget function

class Budget:
        def __init__(self, budget_category, budget_amount):
            self.budget_category = budget_category
            self.budget_amount = budget_amount

def add_budget():
# ask user for the budget in that category
    budget_c = input("What is this budget for?\n")
    budget_a = input(f"What is the budget for {budget_c}?\n")
    budget = Budget(budget_c, budget_a)
    "put budget category in csv"
    return budget

def budget_menu():
    while True:
        choice = input("What would you like to do?\n1.) Create Budget\n2.) Quit\n")

        if choice == "1":
            add_budget()
        
        elif choice == "2":
            quit()
        else:
            print("Please enter valid input.")
            continue

budget_menu()