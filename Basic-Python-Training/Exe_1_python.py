#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 3
##PROBLEM STATEMENT:
#    Write a Python program to display the current date and time.

# Python Version : 3.7
############################################################################################################

"""
    Sample Output :
    Current date and time : 2014-07-05 14:34:14

"""


#################

# Code Here
from datetime import date, datetime

today=date.today()

time=datetime.now()
curr_time=time.strftime("%H:%M:%S")
print(today,curr_time)

#################
