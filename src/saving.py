# DJ, 1st, Saving Program
import customtkinter as ctk
# create saving plan function:
def create_saving_plan():
    current_widget = []
    helper = ctk.CTk
    def clear_windows(helper):
        #Destroys all currently packed widgets in the main window.
        for widget in current_widget:
            widget.destroy()
            current_widget.clear()

    
    # ask user what amount theyre saving to
    while True:
        clear_windows(helper)
        name_entry = ctk.CTkEntry(helper, placeholder_text="Enter the amount you are saving...", width=250)
        name_entry.pack(pady=10)
        current_widget.append(name_entry)
        saving_amount = name_entry.get()

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



        