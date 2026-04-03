# LD 1st
import hashlib
import csv
# This has the functions for signing in and signing up

# Sign up Function
    # This will take in a username that the user wants to use. I will then go into the information csv to compare to the first column (which should be usernames) and check if the username is unique (username != csv name is TRUE). If the username is unique I will ask for a password and HASH it so that I can compare it to the HASHED passwords in the CSV column 2(the hased passwords). I will then check if the HASHED password is unique, and if it is, tell the user sign up is sucessful and create a separate CSV for them. (maybe we have a variable that is the name of the active CSV and I return that)

    # I want password requirements: 12+ characters long, 1+ number, 1+ UPPERCASE,  1+ lowercase, 1+ special character
def sign_up(typed_user, typed_pass):
    # Get username
    while True:
        username = typed_user.strip()
        user_avaliable = item_avaliable(username, 0)
        if user_avaliable == True:
            # Valid username, break to do the password
            break
        else:
            print("It seems that the username you typed is already taken. Enter something else.")
            continue
    # Get password
    while True:
        the_password = typed_pass.strip()
        pass_valid = pass_requirements(the_password)
        if pass_valid == True:
            # password meets requirements. Now check if password avaliable
            pass
        else:
            print("Your password doesn't have the nessisary requirements. Please enter a different password")
            continue
        pass_avaliable = item_avaliable(the_password, 1)
        if pass_avaliable == True:
            # password avaliable and meets requirements. Break so that info can be added to user_login_info CSV
            break
        else:
            print("It seems that the password you typed has already been taken. Please enter a different password")
            continue
    # Add info to CSV
    hashed_pass = hash_item(the_password) # get the entered password hashed
    try:
        with open("docs/user_login.csv", "a", newline="") as csv_file:
            fieldnames = ['username', 'password', 'csv_name']
            writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            writer.writerow({'username': username, 'password': hashed_pass, 'csv_name': username})
    except Exception as reason:
        print(f"Could not open file in SIGN_UP func. Reason: {reason}")
    
    # Now create a CSV for this user
    try:
        with open(f"docs/{username}.csv", "w", newline="") as user_file:
            fieldnames = ['day', 'month', 'year', 'income', 'expense', 'food', 'savings']
            this_writer = csv.DictWriter(user_file, fieldnames=fieldnames)
            this_writer.writeheader()
    except Exception as e:
        print(f"Could not make user file in SIGN_UP func. Reason: {e}")
    
    # The username is what is used to create a CSV for that user. Returning the current CSV name so that it can be used else where
    current_csv = f"docs/{username}.csv"
    return current_csv

# Sign in Function
    # This will take in a username AND a password (HASH IT). Then go into the information csv and for each line, check if both username AND HASHED password MATCH(column 0 and 1) the given information. If both match, get the csv name FROM THE SAME ROW and save it as current CSV variable(?). Tell user that they have successfully signed in.
def sign_in(typed_user, typed_pass):
    while True:
        # Get the username and password
        username = typed_user.strip()
        password = typed_pass.strip()
        # hash the password
        hashed_pass = hash_item(password)
        try:
            # open the user_login_info file to compare
            with open("docs/user_login_info.csv", "r") as file:
                # default is no match
                match = False
                reader = csv.reader(file)

                for row in reader:
                    if row[0] == username and row[1] == hashed_pass:
                        # There is a match. Also gab the csv name for this user
                        match == True
                        current_csv = row[2]
                        break
                    else:
                        continue
        except Exception as e:
            print(f"Could not open file in SIGN_IN func. Reason: {e}")
        
        # Finished with the file. Now check if there was a match
        if match == True:
            # There was a match. return the csv name for this signed in user
            print("Signed in successfully.")
            return current_csv
        else:
            print("Username and/or password incorrect. Please try again")
            continue

# HELPERS
def pass_requirements(password):
    score = 0
    special_charcters = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", '"', "'", "<", ">", ",", ".", "?", "/"]
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    # Getting requirements
    if len(password) >= 1 and len(password) <= 40:
        score += 1
    if uppercase == True:
        score += 1
    if lowercase == True:
        score += 1
    if digit == True:
        score += 1
    if " " not in password:
        # I think that passwords should have no spaces
        score += 1
    for char in password:
        if char in special_charcters:
            score +=1 
            break
    # Requirments aquired. Now check if the score is a certain value. Return true if it is
    if score >= 6:
        return True
    else:
        return False

def hash_item(hash_item):
    encoded_string = hash_item.encode('utf-8')
    hash_object = hashlib.sha256()
    hash_object.update(encoded_string)
    hex_hash = hash_object.hexdigest()
    return hex_hash

def item_avaliable(string, column):
    # I need CSV to work on this
    # First, if column == 0, this is USERNAME
    # If column == 1, this is PASSWORD and I need to access the key to hash the given string BEFORE comparing
    # Open file first
    avaliable = True
    csv_file = open("docs/user_login_info.csv", 'r', newline='')
    csv_reader = csv.DictReader(csv_file)
    if column == 0:
        for line in csv_reader:
            if string == line['username']:
                avaliable = False # found a match meaning item is not unique
                break
            else:
                continue
    elif column == 1:
        for line in csv_reader:
            # First, hash the string (should be password)
            final_hash = hash_item(string)
            if final_hash == line['password']:
                # Found a match. Invalid
                avaliable = False
                break
            else:
                continue
    else:
        print("What the hell?")  
    return avaliable 