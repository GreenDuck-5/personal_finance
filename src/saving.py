# DJ, 1st, Saving Program

# create saving plan function:
def create_saving_plan():

    # ask user what amount theyre saving to
    while True:
        saving_amount = input("What amount are you saving to?\n")
        
        if saving_amount.isdigit():
            saving_amount = int(saving_amount)
            break
        else:
            print("Please enter valid input")
            continue
    
    
    # ask user how much money theyre putting in and how often
    while True:
        deposit_often = input("How often are you going to put money in? (You'll decide how much you'll deposit next)\n1.) Daily\n2.) Weekly\n3.) Monthly\n")
        
        if deposit_often == "1":
            deposit_often = "daily"
            break
        elif deposit_often == "2":
            deposit_often = "weekly"
            break
        elif deposit_often == "3":
            deposit_often = "monthly"
            break
        else:
            print("Please enter valid input")
            continue

    often = ("daily", "weekly", "yearly")

    while True:
        deposit_amount = input(f"How much money are you going to put in every {deposit_often}?\n").lower()
        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            break
        else:
            print("Please enter valid input")
            continue

    # find monthly expense and add that as a budgetting category
    if deposit_often == "daily":
        monthly_expense = (deposit_amount * 30)
    elif deposit_often == "weekly":
        monthly_expense = (deposit_amount * 4)
    elif deposit_often == "monthly":
        monthly_expense = deposit_amount
    
    saving_time = saving_amount / monthly_expense

    return saving_amount, deposit_often, deposit_amount, monthly_expense, saving_time


# view saving plan function:
def view_saving(saving_amount, deposit_often, deposit_amount, monthly_expense, saving_time):
    print(f"""Your current saving plan is:
How much are you saving to?: {saving_amount}
How often are you adding money?: {deposit_often}
How much are you putting in?: {deposit_amount}
What is the monthly expense?: {monthly_expense}
How long until finished saving?: {saving_time} months
          """)
    # give user option to edit the saving plan or quit
    change = input("Do you want to edit the saving plan? y/n\n").lower()
    # if user picks to edit
    if change == "y":
        create_saving_plan()

#main menu function
def saving_menu():
    while True:
        #ask user what they would like to do: create saving plan, view saving plan, quit
        choice = input("1: Create Saving Plan\n2: View Saving Plan\n3: Quit\n").strip()

        # if user picks create: run create saving plan function
        if choice == "1":
            saving_amount, deposit_often, deposit_amount, monthly_expense, saving_time = create_saving_plan()

    # if user picks view: run view saving plan function
        elif choice == "2":
            view_saving(saving_amount, deposit_often, deposit_amount, monthly_expense, saving_time)

    # if user picks quit: go back to main menu
        else:
            "return to main menu"
            break

saving_menu()
