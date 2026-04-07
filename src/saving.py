# DJ, 1st, Saving Program

from datetime import datetime
import time as t

# create saving plan function:
def create_saving_plan():

    # ask user what amount theyre saving to
    while True:
        saving_amount = input("What amount are you saving to?\n")
        
        if saving_amount.isdigit():
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

    while True:
        deposit_amount = input(f"How much money are you going to put in every {deposit_often}?\n")
        if deposit_amount.isdigit():
            break
        else:
            print("Please enter valid input")
            continue

    # find monthly expense and add that as a budgetting category
    if deposit_often == "daily":
        monthly_expense = (deposit_amount * 30) / saving_amount
    elif deposit_often == "weekly":
        monthly_expense = (deposit_amount * 4) / saving_amount
    elif deposit_often == "monthly":
        monthly_expense = deposit_often / saving_amount


# view saving plan function:

    # show list of saving plans

    # let user pick one and view its details

    # give user option to edit the saving plan or quit

    # if user picks to edit

        # let user change the details of each plan


#main menu function
def saving_menu():
    #ask user what they would like to do: create saving plan, view saving plan, quit
    choice = input("1: Create Saving Plan\n2: View Saving Plan\n3: Quit\n").strip()

    # if user picks create: run create saving plan function
    match choice:
        case "1":
            pass

    # if user picks view: run view saving plan function


    # if user picks quit: go back to main menu




