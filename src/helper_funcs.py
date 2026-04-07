# File to hold any and all helper functions
import time

def is_num(potential_num):
    try:
        int(potential_num)
        return True
    except:
        return False
    
def type_print(string, delay = 0.06):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)