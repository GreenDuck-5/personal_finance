import time

def is_num(potential_num):
    """Check if the string can be converted to a number (int or float)."""
    try:
        float(potential_num)
        return True
    except:
        return False

def type_print(string, delay=0.06):
    """Prints characters with a delay for a typing effect."""
    for char in string:
        print(char, end="", flush=True)
        time.sleep(delay)