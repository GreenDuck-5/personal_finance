# DJ, 1st, Saving Program


# create saving plan function:
def create_saving_plan():

    # ask user what amount theyre saving to
    while True:
        choice = input("What amount are you saving to?\n")
        
        if choice.isdigit():
            break
        else:
            print("Please enter valid input")
    
    # ask user how much money theyre putting in and how often
    

    # find monthly expense and add that as a budgetting category



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




