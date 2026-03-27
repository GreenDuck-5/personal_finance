# LD 1st
# This has the functions for signing in and signing up

# Sign up Function
    # This will take in a username that the user wants to use. I will then go into information.csv to compare to the first column (which should be usernames) and check if the username is unique (username != csv name is TRUE). If the username is unique I will ask for a password and HASH it so that I can compare it to the HASHED passwords in the CSV column 2. I will then check if the HASHED password is unique, and if it is, tell the user sign up is sucessful and create a separate CSV for them. (maybe we have a variable that is the name of the active CSV and I return that)

    # I want password requirements: 12+ characters long, 1+ number, 1+ UPPERCASE,  1+ lowercase, 1+ special character

# Sign in Function
    # This will take in a username AND a password (HASH IT). Then go into information.csv and for each line, check if both username AND HASHED password MATCH. If both match, get the csv name FROM THE SAME ROW and save it as current CSV variable(?). Tell user that they have successfully signed in.