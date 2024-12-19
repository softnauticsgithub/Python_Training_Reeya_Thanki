#Topic : BASIC PYTHON
#Exercise Number : 3
##PROBLEM STATEMENT:
#    Write a Python program to display the current date and time.
# Python Version : 3.7
"""
    Sample Output :
    Current date and time : 2014-07-05 14:34:14
"""
from datetime import date, datetime
today_curr=date.today()
time_curr=datetime.now()
curr_time=time_curr.strftime("%H:%M:%S")
print(today_curr,curr_time)
