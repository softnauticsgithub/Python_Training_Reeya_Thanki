#Topic : BASIC PYTHON
#Exercise Number : 18
##PROBLEM STATEMENT:
#Python code to demonstrate the exception handling.
# Make sure your code print the detailed exception traceback
#and also write all the exception occured to a specific file.
# Python Version : 3.7
'''
here i attach  the code of exception handling
'''
import traceback
A = [1, 2, 3, 4]
try:
    value = A[5]
except IndexError as err:
    traceback.print_exc()
    with open("Exception.txt",'w') as Exception_file:
        Exception_file.write(type(err).__name__)
A = 4
B= 0
try:
    value = A / B
except ZeroDivisionError as err:
    traceback.print_exc()
    with open("Exception.txt",'a+') as Exception_file:
        Exception_file.write(type(err).__name__)
