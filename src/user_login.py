import hashlib
import csv

def sign_up(typed_user, typed_pass):
    username = typed_user.strip()
    password = typed_pass.strip()

    if not item_available(username, 0):
        print("Username already taken. Please choose another.")
        return None, False

    if not pass_requirements(password):
        print("Password doesn't meet the requirements.")
        return None, False

    if not item_available(password, 1):
        print("Password already used. Please choose a different one.")
        return None, False

    hashed_pass = hash_item(password)

    try:
        with open("docs/user_login_info.csv", "a", newline='') as csv_file:
            fieldnames = ['username', 'password', 'csv_name']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_file.seek(0)
            if csv_file.tell() == 0:
                writer.writeheader()
            writer.writerow({'username': username, 'password': hashed_pass, 'csv_name': f"docs/{username}.csv"})
    except Exception as e:
        print(f"Could not open file in SIGN_UP. Reason: {e}")
        return None, False

    try:
        with open(f"docs/{username}.csv", "w", newline='') as user_file:
            fieldnames = ['day', 'month', 'year', 'income', 'expense', 'food', 'savings']
            writer = csv.DictWriter(user_file, fieldnames=fieldnames)
            writer.writeheader()
    except Exception as e:
        print(f"Could not create user CSV. Reason: {e}")
        return None, False

    current_csv = f"docs/{username}.csv"
    return current_csv, True

def sign_in(typed_user, typed_pass):
    username = typed_user.strip()
    password = typed_pass.strip()
    current_csv = None
    matched = False
    hashed_pass = hash_item(password)

    try:
        with open("docs/user_login_info.csv", "r", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username and row['password'] == hashed_pass:
                    current_csv = row['csv_name']
                    matched = True
                    break
    except Exception as e:
        print(f"Could not open user_login_info.csv. Reason: {e}")

    if matched:
        print("Signed in successfully.")
        return current_csv, True
    else:
        print("Username and/or password incorrect.")
        return None, False

def pass_requirements(password):
    special_characters = set("`~!@#$%^&*()_-+={}[]|\\:;\"'<>,.?/")
    if len(password) < 12 or len(password) > 40:
        return False
    if ' ' in password:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in special_characters for c in password):
        return False
    return True

def hash_item(item):
    return hashlib.sha256(item.encode('utf-8')).hexdigest()

def item_available(string, column):
    try:
        with open("docs/user_login_info.csv", 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                if column == 0:
                    if line['username'] == string:
                        return False
                elif column == 1:
                    hashed = hash_item(string)
                    if line['password'] == hashed:
                        return False
        return True
    except Exception as e:
        print(f"Error checking availability: {e}")
        return False