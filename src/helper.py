#isaac stuff here
#import time
import csv
thing = amount, place #placeholder
import time
#def find_timestamp():
def timestamp():
    #When money comes in, run it throught this function to find it's timestamp, and then write it to money.csv
    #curr = time.ctime(time.time())
    curr = time.ctime(time.time())
    #print("Current time:", curr)
    info = (curr, thing)#Whatever the thing iscalled
    #whatever the thing coming in will be called, just say timestamp.

#when spending and income data comes in or goes out, take amount, date, and source, a+ to money.csv.
with open('docs/money.csv', mode='a+', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(info)